import win32con
import ctypes.wintypes
from io import BytesIO
from PIL import Image
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QBuffer
FindWindow = ctypes.windll.user32.FindWindowW
SendMessage = ctypes.windll.user32.SendMessageW


class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ('dwData', ctypes.wintypes.LPARAM),
        ('cbData', ctypes.wintypes.DWORD),
        ('lpData', ctypes.c_char_p)
        # formally lpData is c_void_p, but we do it this way
    ]


class CopydataSender:
    def __init__(self, class_name, window_name):
        self.cl_name = class_name
        self.w_name = window_name

    def send_message(self, msg, msg_type: int):
        hwnd = FindWindow(self.cl_name, self.w_name)
        if not hwnd:
            mes = QMessageBox(text='Подключение не установрлено')
            mes.show()
            return None
        cds = COPYDATASTRUCT()
        cds.dwData = msg_type
        cds.cbData = ctypes.sizeof(ctypes.create_string_buffer(msg))
        cds.lpData = ctypes.c_char_p(msg)
        SendMessage(hwnd, win32con.WM_COPYDATA, 0, ctypes.byref(cds))

    def send_text(self, text):
        self.send_message(text.encode('utf-8'), 0)

    def send_record(self, rec):
        text = str(rec)
        self.send_message(text.encode('utf-8'), 2)

    def send_image(self, data):
        self.send_message(data, 1)

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


if __name__ == '__main__':
    text = 'Ауф'
    CopydataSender('TReceiverMainForm', 'ReceiverMainForm').send_text(text)
