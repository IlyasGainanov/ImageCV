import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi  # не обращай внимания
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from main_window import Ui_MainWindow

filename = " "

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.quit.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.start_file_dialog)
        self.searchBtn.clicked.connect(self.exec)

    def start_file_dialog(self):
        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);")
        filename = file
        if check:
            self.display_img(file)

    def display_img(self, img):
        pixmap = QPixmap(img)
        self.img.setPixmap(pixmap)
        self.show()

    def exec(self, file_name):
        self.label.setText("Медведи находятся где-то в выделенных областях")
        self.show()

        filename = QFileDialog.getOpenFileName()

        print(filename[0])

        img = cv.imread(filename[0])
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        upper = (35, 52, 163)
        lower = (20, 10, 101)

        mask = cv.inRange(hsv, lower, upper)

        plt.imshow(mask)
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
