from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel, QStackedWidget, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QPushButton)
import sys


class DashBoard(QWidget):
    def __init__(self, parent):
        super(DashBoard, self).__init__(parent)

        self.layout = QGridLayout()

        self.NameLBL = QLabel('<font size="4"> Username: </font>')
        self.NameLBL.setFixedWidth(100)
        self.layout.addWidget(self.NameLBL, 0, 2)

        self.NameFieldLBL = QLabel()
        self.NameFieldLBL.setFixedWidth(100)
        self.layout.addWidget(self.NameFieldLBL, 0, 3)

        self.EnrollNoLBL = QLabel('<font size="4"> User Id: </font>')
        self.EnrollNoLBL.setFixedWidth(100)
        self.layout.addWidget(self.EnrollNoLBL, 0, 0)

        self.EnrollNoFieldLBL = QLabel()
        self.EnrollNoFieldLBL.setFixedWidth(100)
        self.layout.addWidget(self.EnrollNoFieldLBL, 0, 1)

        self.setLayout(self.layout)