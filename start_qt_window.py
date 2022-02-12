import sys

from PyQt5 import QtGui, uic, QtMultimedia, QtCore
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QTableWidgetItem

from get_image import get_image


class HelloScreen(QWidget):
    def __init__(self):
        super(HelloScreen, self).__init__()
        uic.loadUi("start_qt_window.ui", self)
        self.show()

        self.start_button.clicked.connect(self.get_data)

    def get_data(self):
        longitude = self.longitude.text()
        latitude = self.latitude.text()
        scale = self.scale.text()

        ll = ",".join(map(str, [longitude, latitude]))
        scale = ",".join(map(str, (scale,) * 2))

        get_image(ll, scale)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


def start_application():
    app = QApplication(sys.argv)
    ex = HelloScreen()
    sys.exit(app.exec())
