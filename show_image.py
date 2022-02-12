import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton
from get_image import get_image

SCREEN_SIZE = [600, 550]



class ImageWindow(QWidget):
    def __init__(self, image, ll, scale):
        super().__init__()
        self.longitude, self.latitude = ll.split(',')
        self.longitude, self.latitude = float(self.longitude), float(self.latitude)
        self.scale = float(scale.split(',')[0])
        self.scheme = 'map'
        self.file_name = image
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap(self.file_name)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

        self.scheme_button = QRadioButton(self)
        self.scheme_button.move(30, 460)
        self.scheme_button.resize(200, 50)
        self.scheme_button.setText("Схема")
        self.scheme_button.setChecked(True)
        self.satellite_button = QRadioButton(self)
        self.satellite_button.move(200, 460)
        self.satellite_button.resize(200, 50)
        self.satellite_button.setText("Спутник")
        self.hybrid_button = QRadioButton(self)
        self.hybrid_button.move(350, 460)
        self.hybrid_button.resize(200, 50)
        self.hybrid_button.setText("Гибрид")

        self.scheme_button.toggled.connect(self.change_scheme)
        self.satellite_button.toggled.connect(self.change_scheme)
        self.hybrid_button.toggled.connect(self.change_scheme)

    def change_scheme(self):
        if self.scheme_button.isChecked():
            self.scheme = 'map'
        elif self.satellite_button.isChecked():
            self.scheme = 'sat'
        elif self.hybrid_button.isChecked():
            self.scheme = 'sat,skl'
        self.update_image()


    def update_image(self):
        ll = ",".join(map(str, [self.longitude, self.latitude]))
        scale = ",".join(map(str, (self.scale,) * 2))
        #self.pixmap = QPixmap.fromImage(get_image(ll, scale, map_type=self.scheme))
        self.pixmap = QPixmap(get_image(ll, scale, map_type=self.scheme))
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

        self.update_image()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.file_name)





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

