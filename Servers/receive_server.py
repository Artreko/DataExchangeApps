import sys
import math
import socket
import locale
import os
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QThread, pyqtSlot, pyqtSignal, QRunnable, QObject
from UI.server_ui import Ui_ReceiveServerForm
import traceback
from Record.record import DataRec
from dotenv import load_dotenv
from datetime import date
from io import BytesIO
import pyperclip3
from PIL import ImageGrab, Image
from Senders.socket_sender import SocketSender
import datetime


load_dotenv()
HOST = os.getenv('HOST')
SERVER_PORT = int(os.getenv('SOCKET_SERVER_PORT'))
SEND_FRAME = int(os.getenv('SEND_FRAME'))
DB_PORT = int(os.getenv('DB_SERVER_PORT'))


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)

    sys.exit()


sys.excepthook = log_uncaught_exceptions


class WorkerSignals(QObject):
    received_text = pyqtSignal(str)
    received_record = pyqtSignal(DataRec)
    received_image = pyqtSignal(QPixmap)


class SocketWorker(QThread):
    def __init__(self, host: str, port: int):
        super(SocketWorker, self).__init__()
        self.host = host
        self.port = port
        self.signals = WorkerSignals()

    def run(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(2)
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                continue
            command = data.decode('utf-8')
            match command:
                case 'SEND_RECORD':
                    data = conn.recv(1024).decode('utf-8')
                    self.get_record(data)
                case 'SEND_IMAGE':
                    size = conn.recv(1024)
                    print(size)
                    size = size.decode('utf-8')
                    size = int(size)
                    conn.send(b'READY')
                    with BytesIO() as buf:
                        for _ in range(math.ceil(size / SEND_FRAME)):
                            data = conn.recv(SEND_FRAME)
                            buf.write(data)
                        buf.seek(0)
                        data = buf.read()
                        self.get_image(data)
                case _:
                    self.signals.received_text.emit(command)

    def get_record(self, data: str):
        data = data.split(';')
        name = data[0]
        exp = int(data[1])
        birth = data[2].split('.')
        birth = list(map(int, birth))
        birth = date(birth[2], birth[1], birth[0])
        rec = DataRec(name, exp, birth)
        self.signals.received_record.emit(rec)

    def get_image(self, data: bytes):
        img = QImage.fromData(data, 'BMP')
        pxmap = QPixmap.fromImage(img)
        self.signals.received_image.emit(pxmap)


class App(QWidget):
    start = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReceiveServerForm()
        self.ui.setupUi(self)

        self.socket = SocketSender(HOST, DB_PORT)

        self.ui.clearTextButton.clicked.connect(self.clear_text)
        self.ui.clearRecordButton.clicked.connect(self.clear_record)
        self.ui.clearImageButton.clicked.connect(self.clear_image)

        self.ui.pasteTextButton.clicked.connect(self.paste_text)
        self.ui.pasteRecordButton.clicked.connect(self.paste_record)
        self.ui.pasteImageButton.clicked.connect(self.paste_image)

        self.worker = SocketWorker(HOST, SERVER_PORT)
        self.worker.signals.received_text.connect(self.get_text)
        self.worker.signals.received_record.connect(self.get_record)
        self.worker.signals.received_image.connect(self.get_image)
        self.worker.start()

    def clear_text(self):
        self.ui.textEdit.clear()

    def clear_record(self):
        self.ui.nameEdit.clear()
        self.ui.expSpin.setValue(1)
        self.ui.birthEdit.setDate(date(2000, 1, 1))

    def clear_image(self):
        self.ui.imageLabel.clear()

    def send_stats(self, op_id, mes_id):
        self.socket.send_text(f'{op_id} {mes_id} {datetime.datetime.now().isoformat()} \n')

    def get_text(self, text):
        self.set_text(text)
        self.send_stats(2, 1)

    def set_text(self, text):
        self.ui.textEdit.setText(text)

    def get_record(self, rec: DataRec):
        self.set_record(rec)
        self.send_stats(2, 3)

    def set_record(self, rec: DataRec):
        self.ui.nameEdit.setText(rec.name)
        self.ui.expSpin.setValue(rec.work_years)
        self.ui.birthEdit.setDate(rec.birth_date)

    def get_image(self, pxmap):
        self.set_image(pxmap)
        self.send_stats(2, 2)

    def set_image(self, pxmap: QPixmap):
        self.ui.imageLabel.setPixmap(pxmap)

    def paste_text(self):
        try:
            text = pyperclip3.paste()
            text = text.decode('utf-8')
            self.set_text(text)
            self.send_stats(1, 1)
        except UnicodeDecodeError:
            QMessageBox.critical(self, 'Error', 'Не удалось декодировать')

    def paste_record(self):
        try:
            text = pyperclip3.paste()
            text = text.decode('utf-8')
            if 'record:' in text:
                data = text[len('record:'):].split(';')
                name = data[0]
                exp = int(data[1])
                birth = data[2].split('.')
                birth = list(map(int, birth))
                birth = date(birth[2], birth[1], birth[0])
                rec = DataRec(name, exp, birth)
                self.set_record(rec)
                self.send_stats(1, 3)
        except UnicodeDecodeError:
            QMessageBox.critical(self, 'Error', 'Не удалось декодировать')

    def paste_image(self):
        im = ImageGrab.grabclipboard()
        if not im:
            return None
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
            # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
        pixmap = QPixmap.fromImage(qim)
        self.set_image(pixmap)
        self.send_stats(1, 2)


def main():
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    main_window.move(715, 80)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
