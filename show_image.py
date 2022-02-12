import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


def show_image(image):
    class ImageWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(100, 100, *SCREEN_SIZE)
            self.setWindowTitle('Отображение карты')

            ## Изображение
            self.pixmap = QPixmap(image)
            self.image = QLabel(self)
            self.image.move(0, 0)
            self.image.resize(600, 450)
            self.image.setPixmap(self.pixmap)

        def closeEvent(self, event):
            """При закрытии формы подчищаем за собой"""
            os.remove(self.map_file)


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = ImageWindow()
        ex.show()
        sys.exit(app.exec())

