import os
import socket
from PyQt6.QtCore import QBuffer
from PyQt6.QtWidgets import QMessageBox
from io import BytesIO
from dotenv import load_dotenv


load_dotenv()
SEND_FRAME = int(os.getenv('SEND_FRAME'))


class SocketSender:
    def __init__(self, host: str, port: int) -> None:
        self.socket = socket.socket()
        self.host = host
        self.port = port
        self.connected = False
        self.connect()

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            self.connected = True
        except ConnectionRefusedError:
            self.connected = False
            mes = QMessageBox(
                text='Подключение к серверу не установрлено'
            )
            return False
        return True

    def send_text(self, text):
        if self.connected or self.connect():
            self.socket.send(text.encode('utf-8'))
            # self.socket.send(text)

    def send_record(self, rec):
        self.send_text("SEND_RECORD")
        self.send_text(str(rec))

    def send_image(self, image):
        self.send_text('SEND_IMAGE')
        self.send_text(f'{len(image)}')
        if self.socket.recv(1024) == b'READY':
            with BytesIO(image) as buf:
                buf.seek(0)
                chunk = buf.read(SEND_FRAME)
                while chunk:
                    self.socket.send(chunk)
                    chunk = buf.read(SEND_FRAME)

    def convert_qimage(self, image):
        qbuf = QBuffer()
        # qbuf.open(qbuf.openMode().ReadWrite)
        # image.save(qbuf, 'BMP')
        qbuf.open(qbuf.openMode().ReadWrite)
        image.save(qbuf, 'BMP')
        with BytesIO(qbuf.data()) as output:
            output.seek(0)
            data = output.read()
        qbuf.close()
        return data

    def exit(self):
        self.socket.send(b'exit')
