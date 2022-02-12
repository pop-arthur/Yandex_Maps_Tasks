import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from get_image import get_image

SCREEN_SIZE = [600, 450]



class ImageWindow(QWidget):
    def __init__(self, image, ll, scale):
        super().__init__()
        self.initUI(image)
        self.longitude, self.latitude = ll.split(',')
        self.longitude, self.latitude = float(self.longitude), float(self.latitude)
        self.scale = float(scale.split(',')[0])
        print(self.longitude, self.latitude, self.scale)

    def initUI(self, image):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap.fromImage(image)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.scale *= 2
        if event.key() == Qt.Key_PageDown:
            self.scale /= 2
        if event.key() == Qt.Key_Left:
            self.longitude -= 1
        if event.key() == Qt.Key_Right:
            self.longitude += 1
        if event.key() == Qt.Key_Up:
            self.latitude += 1
        if event.key() == Qt.Key_Down:
            self.latitude -= 1
        ll = ",".join(map(str, [self.longitude, self.latitude]))
        scale = ",".join(map(str, (self.scale,) * 2))
        self.pixmap = QPixmap.fromImage(get_image(ll, scale))
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

