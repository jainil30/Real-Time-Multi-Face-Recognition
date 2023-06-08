from PyQt5.QtCore import *
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QPushButton)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import mysql.connector
import sys

from BackEnd.Login import *
from BackEnd.SignUpManager import *

class Start(QWidget):

    def __init__(self, parent=None):
        super(Start, self).__init__(parent)

        self.layout = QGridLayout()

        self.button_login = QPushButton('Login Page')
        self.button_login.setFixedWidth(100)
        self.layout.addWidget(self.button_login,0,0)

        self.button_signup = QPushButton('Sign Up Page')
        self.button_signup.setFixedWidth(100)
        self.layout.addWidget(self.button_signup,0,1)

        self.stackArea = QStackedWidget()
        self.login_screen = LoginWidget(self)
        self.signup_screen = SignUpWidget(self)

        self.stackArea.addWidget(self.login_screen)
        self.stackArea.addWidget(self.signup_screen)

        self.stackArea.setCurrentWidget(self.login_screen)

        self.button_login.clicked.connect(lambda: self.stackArea.setCurrentWidget(self.login_screen))
        self.signup_screen.signUpSuccess.connect(lambda: self.stackArea.setCurrentWidget(self.login_screen))
        self.button_signup.clicked.connect(lambda: self.stackArea.setCurrentWidget(self.signup_screen))

        self.layout.addWidget(self.stackArea,1,0,1,2)
        self.setLayout(self.layout)


class LoginWidget(QWidget):
    loginCorrect = pyqtSignal()
    loginManager = LoginManager()
    name = ""
    id = 0
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)

        layout = QGridLayout()

        self.label_name = QLabel('<font size="4"> User ID: </font>')
        # self.label_name.setFixedWidth(100)

        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your User Id')
        # self.lineEdit_username.setFixedWidth(100)

        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        self.label_password = QLabel('<font size="4"> Password: </font>')
        # self.label_password.setFixedWidth(100)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        # self.lineEdit_password.setFixedWidth(100)
        layout.addWidget(self.label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        self.button_login = QPushButton('Login')
        self.button_login.clicked.connect(self.check_password)
        # self.button_login.setFixedWidth(200)
        layout.addWidget(self.button_login, 2, 0, 1, 2)
        # layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        isUser = self.loginManager.checkLoginCredentials(self.lineEdit_username.text(),
                                                self.lineEdit_password.text())

        print(isUser)
        if isUser != -2:
            msg.setWindowTitle("Login Result")
            msg.setText('Success')
            msg.exec_()
            self.name = isUser[1]
            self.id = isUser[0]
            self.loginCorrect.emit()
        else:
            msg.setWindowTitle("Login Result")
            msg.setText('Incorrect Password')
            msg.exec_()

class SignUpWidget(QWidget):
    newOperator = SignUpManager()
    signUpSuccess = pyqtSignal()
    def __init__(self, parent=None):
        super(SignUpWidget, self).__init__(parent)

        layout = QGridLayout()

        self.label_opName = QLabel('<font size="4"> Username: </font>')
        # self.label_opName.setFixedWidth(100)

        self.lineEdit_opName = QLineEdit()
        self.lineEdit_opName.setPlaceholderText('Please enter your username')
        # self.lineEdit_opName.setFixedWidth(100)

        layout.addWidget(self.label_opName, 0, 0)
        layout.addWidget(self.lineEdit_opName, 0, 1)

        self.label_opID = QLabel('<font size="4"> Operator ID: </font>')
        # self.label_opID.setFixedWidth(100)

        self.lineEdit_opID = QLineEdit()
        self.lineEdit_opID.setPlaceholderText('Please enter your operator ID')
        # self.lineEdit_opID.setFixedWidth(100)

        layout.addWidget(self.label_opID, 1, 0)
        layout.addWidget(self.lineEdit_opID, 1, 1)

        self.label_opMobile = QLabel('<font size="4"> Operator Mobile: </font>')
        # self.label_opMobile.setFixedWidth(100)

        self.lineEdit_opMobile = QLineEdit()
        self.lineEdit_opMobile.setPlaceholderText('Please enter your operator Mobile')
        # self.lineEdit_opMobile.setFixedWidth(100)

        layout.addWidget(self.label_opMobile, 2, 0)
        layout.addWidget(self.lineEdit_opMobile, 2, 1)

        self.label_opEmail = QLabel('<font size="4"> Operator Email: </font>')
        # self.label_opEmail.setFixedWidth(100)

        self.lineEdit_opEmail = QLineEdit()
        self.lineEdit_opEmail.setPlaceholderText('Please enter your operator Email')
        # self.lineEdit_opEmail.setFixedWidth(100)

        layout.addWidget(self.label_opEmail, 3, 0)
        layout.addWidget(self.lineEdit_opEmail, 3, 1)

        self.label_opCustomerID = QLabel('<font size="4"> Operator Customer ID: </font>')
        # self.label_opCustomerID.setFixedWidth(100)

        self.lineEdit_opCustomerID = QLineEdit()
        self.lineEdit_opCustomerID.setPlaceholderText('Please enter your operator Customer ID')
        # self.lineEdit_opCustomerID.setFixedWidth(100)

        layout.addWidget(self.label_opCustomerID, 4, 0)
        layout.addWidget(self.lineEdit_opCustomerID, 4, 1)

        self.label_opPassword = QLabel('<font size="4"> Password: </font>')
        # self.label_opPassword.setFixedWidth(100)

        self.lineEdit_opPassword = QLineEdit()
        self.lineEdit_opPassword.setPlaceholderText('Please enter your Password')

        layout.addWidget(self.label_opPassword, 5, 0)
        layout.addWidget(self.lineEdit_opPassword, 5, 1)

        # self.lineEdit_opPassword.setFixedWidth(100)

        self.label_conform_opPassword = QLabel('<font size="4">Conform Password: </font>')
        # self.label_opPassword.setFixedWidth(100)

        self.lineEdit_conform_opPassword = QLineEdit()
        self.lineEdit_conform_opPassword.setPlaceholderText('Please enter your Password')
        # self.lineEdit_opPassword.setFixedWidth(100)

        layout.addWidget(self.label_conform_opPassword, 6, 0)
        layout.addWidget(self.lineEdit_conform_opPassword, 6, 1)

        self.button_signUp = QPushButton('SignUp')
        # self.button_login.setFixedWidth(200)
        layout.addWidget(self.button_signUp, 7, 0, 1, 2)
        self.button_signUp.clicked.connect(lambda: self.insertOperator())
        self.setLayout(layout)

    def insertOperator(self):
        msg = QMessageBox()
        msg.setFixedSize(100, 50)
        isSuccess = self.newOperator.addOperator(self.lineEdit_opID.text(),self.lineEdit_opName.text(), self.lineEdit_opMobile.text(), self.lineEdit_opEmail.text(),
                                     self.lineEdit_opCustomerID.text(),
                                     self.lineEdit_opPassword.text(), self.lineEdit_conform_opPassword.text(),
                                     )
        if isSuccess == 0:
            msg.setWindowTitle("Sign Up Result")
            msg.setText("Sign Up Success")
            msg.exec_()
            self.signUpSuccess.emit()
        elif isSuccess == -1:
            msg.setWindowTitle("Sign Up Result")
            msg.setText("ID is already registerd")
            msg.exec_()
        else:
            msg.setWindowTitle("Sign Up Result")
            msg.setText("Please check the fields!")
            msg.exec_()
