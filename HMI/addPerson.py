# import system module
import sys
import cv2
import numpy as np
from PIL import Image
import os

from PyQt5 import QtCore, QtGui, QtWidgets
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# # import Opencv module
import cv2

from BackEnd.addPersonManager import *

class AddPerson(QWidget):
    # class constructor
    count = 0

    font = cv2.FONT_HERSHEY_SIMPLEX
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')

    def __init__(self, parent=None):
        super(AddPerson, self).__init__(parent)
        # self.centralwidget = QWidget(MainWindow)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # load face cascade classifier
        self.face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml')
        if self.face_cascade.empty():
            QMessageBox.information(self, "Error Loading cascade classifier",
                                    "Unable to load the face	cascade classifier xml file")
            sys.exit()

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.detectFaces)

        # set control_bt callback clicked  function
        self.ui.camera_area.control_bt.clicked.connect(self.controlTimer)

        # MainWindow.setCentralWidget(self.centralwidget)

    # Function to label the images
    def getImageAndLabels(self):
        # Path to images
        path = "dataset"
        detector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt.xml")
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        facesamples = []
        ids = []

        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')

            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])

            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                facesamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        self.recognizer.train(facesamples, np.array(ids))
        self.recognizer.write('trainer/trainer.yml')

    # detect face
    def detectFaces(self):
        # read frame from video capture
        ret, frame = self.cap.read()

        # recognizer = cv2.face.LBPHFaceRecognizer_create()

        # resize frame image
        scaling_factor = 0.5
        frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

        # convert frame to GRAY format
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect rect faces
        face_rects = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        # for all detected faces
        for (x, y, w, h) in face_rects:
            # draw green rect on face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if self.count < 351 :
                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/Person." + self.ui.addDetails_area.lineEdit_opID.text() + '.' + str(self.count) + ".jpg", gray[y:y + h, x:x + w])
                self.count+=1
                if self.count == 51:
                    self.getImageAndLabels()

        # convert frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # get frame infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from RGB frame
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show frame in img_label
        self.ui.camera_area.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.camera_area.control_bt.setText("Stop")
            # update count
            self.count = 0
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.camera_area.control_bt.setText("Start")

class Ui_Form(QWidget):
    def setupUi(self, Form):
        # Form.setObjectName("Form")
        # Form.resize(556, 381)
        self.HLayout = QHBoxLayout(Form)

        self.addDetails_area = AddDetails(self)
        self.HLayout.addWidget(self.addDetails_area)

        self.camera_area = CameraView(self)
        self.HLayout.addWidget(self.camera_area)

        QtCore.QMetaObject.connectSlotsByName(Form)

class AddDetails(QWidget):
    personDetail = AddPersonDetails()
    def __init__(self, parent=None):
        super(AddDetails, self).__init__(parent)

        self.layout = QGridLayout()

        self.label_title = QLabel("Enter the following details:")
        self.layout.addWidget(self.label_title,0,0,2,2)

        self.label_opName = QLabel('<font size="4">Name: </font>')
        # self.label_opName.setFixedWidth(100)

        self.lineEdit_opName = QLineEdit()
        self.lineEdit_opName.setPlaceholderText('Please enter your username')
        # self.lineEdit_opName.setFixedWidth(100)

        self.layout.addWidget(self.label_opName, 1, 0)
        self.layout.addWidget(self.lineEdit_opName, 1, 1)

        self.label_opDOB = QLabel('<font size="4">D.O.B: </font>')
        # self.label_opName.setFixedWidth(100)

        self.lineEdit_opDOB = QLineEdit()
        self.lineEdit_opDOB.setPlaceholderText('Please enter your DOB in (YYYY-MM-DD) format')
        # self.lineEdit_opName.setFixedWidth(100)

        self.layout.addWidget(self.label_opDOB, 2, 0)
        self.layout.addWidget(self.lineEdit_opDOB, 2, 1)

        self.label_opMobile = QLabel('<font size="4">Mobile: </font>')
        # self.label_opMobile.setFixedWidth(100)

        self.lineEdit_opMobile = QLineEdit()
        self.lineEdit_opMobile.setPlaceholderText('Please enter your Mobile')
        # self.lineEdit_opMobile.setFixedWidth(100)

        self.layout.addWidget(self.label_opMobile, 3, 0)
        self.layout.addWidget(self.lineEdit_opMobile, 3, 1)

        self.label_opEmail = QLabel('<font size="4">Email: </font>')
        # self.label_opEmail.setFixedWidth(100)

        self.lineEdit_opEmail = QLineEdit()
        self.lineEdit_opEmail.setPlaceholderText('Please enter your Email')
        # self.lineEdit_opEmail.setFixedWidth(100)

        self.layout.addWidget(self.label_opEmail, 4, 0)
        self.layout.addWidget(self.lineEdit_opEmail, 4, 1)

        self.label_opAadhar = QLabel('<font size="4">Aadhar no: </font>')
        # self.label_opEmail.setFixedWidth(100)

        self.lineEdit_opAadhar = QLineEdit()
        self.lineEdit_opAadhar.setPlaceholderText('Please enter your Aadhar no')
        # self.lineEdit_opEmail.setFixedWidth(100)

        self.layout.addWidget(self.label_opAadhar, 5, 0)
        self.layout.addWidget(self.lineEdit_opAadhar, 5, 1)

        self.label_opDesignation = QLabel('<font size="4">Designation: </font>')
        # self.label_opEmail.setFixedWidth(100)

        self.lineEdit_opDesignation = QLineEdit()
        self.lineEdit_opDesignation.setPlaceholderText('Please enter your Designation')
        # self.lineEdit_opEmail.setFixedWidth(100)

        self.layout.addWidget(self.label_opDesignation, 6, 0)
        self.layout.addWidget(self.lineEdit_opDesignation, 6, 1)

        self.label_opID = QLabel('<font size="4">ID: </font>')
        # self.label_opEmail.setFixedWidth(100)

        self.lineEdit_opID = QLineEdit()
        self.lineEdit_opID.setPlaceholderText('Please enter your ID')
        # self.lineEdit_opEmail.setFixedWidth(100)

        self.layout.addWidget(self.label_opID, 7, 0)
        self.layout.addWidget(self.lineEdit_opID, 7, 1)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(lambda : self.insertPerson())
        self.layout.addWidget(self.button_submit,8,0,1,2)

        self.setLayout(self.layout)

    def insertPerson(self):
        msg = QMessageBox()
        msg.setFixedSize(100, 50)
        isSuccess = self.personDetail.addPersonDetails(self.lineEdit_opID.text(),self.lineEdit_opName.text(), self.lineEdit_opDesignation.text(), self.lineEdit_opMobile.text(),
                                           self.lineEdit_opEmail.text(), self.lineEdit_opDOB.text(), self.lineEdit_opAadhar.text())

        if isSuccess == 0:
            msg.setWindowTitle("Add Person Result")
            msg.setText("Added Details")
            msg.exec_()
        elif isSuccess == -1:
            msg.setWindowTitle("Add Person Result")
            msg.setText("ID is already registerd")
            msg.exec_()
        else:
            msg.setWindowTitle("Add Person Result")
            msg.setText("Please check the fields!")
            msg.exec_()


class CameraView(QWidget):
    def __init__(self, parent=None):
        super(CameraView, self).__init__(parent)

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setObjectName("image_label")
        self.layout.addWidget(self.image_label)

        self.control_bt = QtWidgets.QPushButton("Start")
        self.control_bt.setObjectName("control_bt")
        self.layout.addWidget(self.control_bt)

        self.setLayout(self.layout)
