# import system module
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

import mysql.connector

class FaceRecognization(QWidget):
    # class constructor
    count = 0
   # names = ['None', 'Soham', 'Papa', 'Ilza', 'Z', 'W']
    font = cv2.FONT_HERSHEY_SIMPLEX
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')

    mydb = mysql.connector.connect(host="localhost", user="root", password="186490316018")
    cursor = mydb.cursor()

    def __init__(self, parent=None):
        super(FaceRecognization, self).__init__(parent)
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
        self.ui.control_bt.clicked.connect(self.controlTimer)

        # MainWindow.setCentralWidget(self.centralwidget)

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

            id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                no = id
                print(id)
                # id = names[id]
                sqlQuery = ("SELECT person_Name FROM rtmfr.person_data WHERE person_Id=" + str(id))
                self.cursor.execute(sqlQuery)
                result = self.cursor.fetchone()
                sqlQuery = ("UPDATE rtmfr.person_data SET person_isRecognized=1 WHERE person_Id=" + str(id))
                self.cursor.execute(sqlQuery)
                self.mydb.commit()
                print(result)
                data = []
                if result is not None:
                    for row in result:
                        data.append(row)
                    for name in data:
                        print('Names : ', name)
                else:
                    name = "You are Unauthorized! Wait for the guards"
                confidence = " {0}%".format(round(100 - confidence))
            else:
                name = "You are Unauthorized! Wait for the guards"
                confidence = "{0}%".format((round(100 - confidence)))
            cv2.putText(frame, name, (x + 5, y - 5), self.font, 1, (255, 255, 255), 2)

        # convert frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # get frame infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from RGB frame
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show frame in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
            # update count
            self.count = 0
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")

class Ui_Form(object):
    def setupUi(self, Form):
        # Form.setObjectName("Form")
        # Form.resize(556, 381)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        # self.image_label.setFixedSize(640,480)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)
        # self.NameTxt = QLineEdit("1")
        # self.verticalLayout.addWidget(self.NameTxt)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Face detection"))
        self.image_label.setText(_translate("Form", "Click on Start to start camera"))
        self.control_bt.setText(_translate("Form", "Start"))