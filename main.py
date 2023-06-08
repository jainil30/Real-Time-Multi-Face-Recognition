from PyQt5.QtCore import *
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout, QHBoxLayout, QPushButton)
import sys

from HMI.loginPage import *
from HMI.addPerson import *
from HMI.dashBoard import *
from HMI.controlBar import *
from HMI.faceRecognition import *
from HMI.viewDetails import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QMainWindow.__init__(self, parent)

        self.setFixedSize(960,480)

        self.main_stack = QStackedWidget()

        self.start_screen = Start(self)
        self.mainApplication = MainApplication(self)

        self.main_stack.addWidget(self.start_screen)
        self.main_stack.addWidget(self.mainApplication)

        self.main_stack.setCurrentWidget(self.start_screen)

        self.start_screen.login_screen.loginCorrect.connect(lambda : self.main_stack.setCurrentWidget(self.mainApplication))
        self.start_screen.login_screen.loginCorrect.connect(
            lambda: self.updateDashBoard())

        self.setCentralWidget(self.main_stack)

    def updateDashBoard(self):
        print("username" , type(self.start_screen.login_screen.name))
        self.mainApplication.dashBoardUI.NameFieldLBL.setText(str(self.start_screen.login_screen.name))
        self.mainApplication.dashBoardUI.EnrollNoFieldLBL.setText(str(self.start_screen.login_screen.id))

class MainApplication(QWidget):

    def __init__(self, parent):
        super(MainApplication, self).__init__(parent)
        self.layout = QGridLayout(self)

        self.dashBoardUI = DashBoard(self)
        self.layout.addWidget(self.dashBoardUI,0,0,1,2)

        self.controlBarUI = ControlBar(self)
        self.layout.addWidget(self.controlBarUI,1,0)

        self.central_widget = QStackedWidget()
        self.addPerson_screen = AddPerson(self)
        self.faceRec_screen = FaceRecognization(self)
        self.viewDetails_screen = ViewDetails(self)
        self.blockDetails_screen = BlockDetails(self)

        self.central_widget.addWidget(self.addPerson_screen)
        self.central_widget.addWidget(self.faceRec_screen)
        self.central_widget.addWidget(self.viewDetails_screen)
        self.central_widget.addWidget(self.blockDetails_screen)

        self.central_widget.setCurrentWidget(self.faceRec_screen)

        self.controlBarUI.addPersonBTN.clicked.connect(
            lambda: self.central_widget.setCurrentWidget(self.addPerson_screen))
        self.controlBarUI.faceRecBTN.clicked.connect(
            lambda: self.central_widget.setCurrentWidget(self.faceRec_screen))
        self.controlBarUI.viewPersonBTN.clicked.connect(
            lambda: self.central_widget.setCurrentWidget(self.viewDetails_screen))
        self.controlBarUI.viewBlockBTN.clicked.connect(
            lambda: self.central_widget.setCurrentWidget(self.blockDetails_screen))

        self.layout.addWidget(self.central_widget,1,1)

        self.setLayout(self.layout)

app = QApplication(sys.argv)
myWindow = MainWindow(None)
myWindow.setWindowTitle("Real Time Multi-Face Recognition")
myWindow.show()
app.exec_()