import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]



class ImageWindow(QWidget):
    def __init__(self, image):
        super().__init__()
        self.initUI(image)

    def initUI(self, image):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap.fromImage(image)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageWindow('map.png')
    ex.show()
    sys.exit(app.exec())

