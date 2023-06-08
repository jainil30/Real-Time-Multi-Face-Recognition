from PyQt5.QtCore import *
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout, QHBoxLayout, QPushButton)
import sys

class ControlBar(QWidget):

    def __init__(self, parent):
        super(ControlBar, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.addPersonBTN = QPushButton("Add Person")
        self.layout.addWidget(self.addPersonBTN)

        self.faceRecBTN = QPushButton("Face Recognition")
        self.layout.addWidget(self.faceRecBTN)

        self.viewPersonBTN = QPushButton("View Person")
        self.layout.addWidget(self.viewPersonBTN)

        self.viewBlockBTN = QPushButton("View BlackList")
        self.layout.addWidget(self.viewBlockBTN)

        self.setLayout(self.layout)