import locale
import os
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from UI.client_ui import Ui_DataExForm
from Senders.clipboard_sender import ClipboardSender
from Senders.copydata_sender import CopydataSender
from Senders.socket_sender import SocketSender
import traceback
from Record.record import DataRec
from dotenv import load_dotenv

load_dotenv()


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)

    sys.exit()


sys.excepthook = log_uncaught_exceptions


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataExForm()
        self.ui.setupUi(self)

        self.methods = {
            "Clipboard": ClipboardSender(),
            'Socket':   SocketSender(os.getenv('HOST'), int(os.getenv('SOCKET_SERVER_PORT'))),
            "Copydata": CopydataSender(os.getenv('WINDOW_CLASS'), os.getenv('WINDOW_NAME')),
        }
        self.ui.sendTextButton.clicked.connect(self.send_text_button_clicked)
        self.ui.sendRecordButton.clicked.connect(self.send_rec_button_clicked)
        self.ui.imagePathButton.clicked.connect(self.img_path_button_clicked)
        self.ui.sendImageButton.clicked.connect(self.send_img_button_clicked)
    ####################################################
    # send buttons

    def send_text_button_clicked(self):
        method = self.ui.listWidget.currentItem().text()
        text = self.ui.textEdit.text()
        self.methods[method].send_text(text)

    def send_rec_button_clicked(self):
        method = self.ui.listWidget.currentItem().text()
        name = self.ui.nameEdit.text()
        exp = self.ui.expSpin.text()
        birth_date = self.ui.birthEdit.date().toPyDate()
        rec = DataRec(name, exp, birth_date)
        self.methods[method].send_record(rec)

    def send_img_button_clicked(self):
        method = self.ui.listWidget.currentItem().text()

        img_path = self.ui.imagePathEdit.text()
        image = self.ui.imageLabel.pixmap().toImage()

        data = self.methods[method].convert_qimage(image)

        self.methods[method].send_image(data)
    ###########################################################

    def img_path_button_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            caption='Выбор картинки',
            directory=os.getcwd(),
            filter="Image Files (*.bmp *.png *.jpg)"
        )
        if file_path:
            self.ui.imageLabel.setPixmap(QPixmap(file_path))
            self.ui.imagePathEdit.setText(file_path)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    main_window.move(15, 30)
    sys.exit(app.exec())
