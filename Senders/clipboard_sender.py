import pyperclip3
# import clipboard
from io import BytesIO
from ctypes import *
from ctypes.wintypes import *
from Record.record import DataRec
from PIL import Image
from PyQt6.QtCore import QBuffer

HGLOBAL = HANDLE
SIZE_T = c_size_t
GHND = 0x0042
GMEM_SHARE = 0x2000

GlobalAlloc = windll.kernel32.GlobalAlloc
GlobalAlloc.restype = HGLOBAL
GlobalAlloc.argtypes = [UINT, SIZE_T]

GlobalLock = windll.kernel32.GlobalLock
GlobalLock.restype = LPVOID
GlobalLock.argtypes = [HGLOBAL]

GlobalUnlock = windll.kernel32.GlobalUnlock
GlobalUnlock.restype = BOOL
GlobalUnlock.argtypes = [HGLOBAL]

CF_DIB = 8

OpenClipboard = windll.user32.OpenClipboard
OpenClipboard.restype = BOOL
OpenClipboard.argtypes = [HWND]

EmptyClipboard = windll.user32.EmptyClipboard
EmptyClipboard.restype = BOOL
EmptyClipboard.argtypes = None

SetClipboardData = windll.user32.SetClipboardData
SetClipboardData.restype = HANDLE
SetClipboardData.argtypes = [UINT, HANDLE]

CloseClipboard = windll.user32.CloseClipboard
CloseClipboard.restype = BOOL
CloseClipboard.argtypes = None


class ClipboardSender:
    @staticmethod
    def send_text(text):
        pyperclip3.copy(text)

    @staticmethod
    def send_record(rec: DataRec):
        ClipboardSender.send_text("record:" + str(rec))

    @staticmethod
    def send_image(data):
        hData = GlobalAlloc(GHND | GMEM_SHARE, len(data))
        pData = GlobalLock(hData)
        memmove(pData, data, len(data))
        GlobalUnlock(hData)

        OpenClipboard(None)
        EmptyClipboard()
        SetClipboardData(CF_DIB, pData)
        CloseClipboard()

    @staticmethod
    def convert_qimage(image):
        qbuf = QBuffer()
        qbuf.open(qbuf.openMode().ReadWrite)
        image.save(qbuf, 'BMP')
        with BytesIO(qbuf.data()) as output:
            data = output.getvalue()[14:]
        qbuf.close()
        return data


if __name__ == '__main__':
    def main():
        text = r'C:\Users\Artik\Documents\UniversityFiles\Semestr 6\SoftwareDesign\Lab5\DataExchange\UI\img.bmp'
        image = Image.open(text)

        with BytesIO() as output:
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]

        clipbrd = ClipboardSender()
        clipbrd.send_image(data)
    main()