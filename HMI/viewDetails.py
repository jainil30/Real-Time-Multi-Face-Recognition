from PyQt5.QtCore import *
from PyQt5.QtWidgets import ( QTableWidget, QTableWidgetItem, QApplication, QMainWindow, QStackedWidget, QWidget,QVBoxLayout, QHBoxLayout, QPushButton)
import sys
import mysql.connector

class ViewDetails(QWidget):
    mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
    cursor = mydb.cursor()

    def __init__(self, parent):
        super(ViewDetails, self).__init__(parent)

        layout = QVBoxLayout()

        self.table_viewDetails = QTableWidget()
        layout.addWidget(self.table_viewDetails)

        self.table_viewUnknownDetails = QTableWidget()
        layout.addWidget(self.table_viewUnknownDetails)

        self.button_refresh = QPushButton("Refresh")
        layout.addWidget(self.button_refresh)

        self.button_refresh.clicked.connect(lambda : self.loadTable())
        self.button_refresh.clicked.connect(lambda : self.loadunTable())

        self.setLayout(layout)

    def loadTable(self):
        self.cursor.execute('SELECT COUNT(*) FROM rtmfr.person_data WHERE person_isRecognized=1')
        rowcount = self.cursor.fetchall()
        print(rowcount[0][0])
        self.table_viewDetails.setRowCount(rowcount[0][0])
        self.table_viewDetails.setColumnCount(6)
        self.table_viewDetails.setHorizontalHeaderItem(0,QTableWidgetItem("ID"))
        self.table_viewDetails.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table_viewDetails.setHorizontalHeaderItem(2, QTableWidgetItem("Designation"))
        self.table_viewDetails.setHorizontalHeaderItem(3, QTableWidgetItem("Mobile Number"))
        self.table_viewDetails.setHorizontalHeaderItem(4, QTableWidgetItem("E-mail ID"))
        self.table_viewDetails.setHorizontalHeaderItem(5, QTableWidgetItem("D.O.B"))

        self.cursor.execute('SELECT * FROM rtmfr.person_data WHERE person_isRecognized=1')
        for row, form in enumerate(self.cursor):
            # self.table_viewDetails.insertRow(row)
            for column, item in enumerate(form):
                    self.table_viewDetails.setItem(row, column, QTableWidgetItem(str(item)))

    def loadunTable(self):
        self.cursor.execute('SELECT COUNT(*) FROM rtmfr.person_data WHERE person_isRecognized=0')
        rowcount = self.cursor.fetchall()
        print(rowcount[0][0])
        self.table_viewUnknownDetails.setRowCount(rowcount[0][0])
        self.table_viewUnknownDetails.setColumnCount(6)
        self.table_viewUnknownDetails.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table_viewUnknownDetails.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table_viewUnknownDetails.setHorizontalHeaderItem(2, QTableWidgetItem("Designation"))
        self.table_viewUnknownDetails.setHorizontalHeaderItem(3, QTableWidgetItem("Mobile Number"))
        self.table_viewUnknownDetails.setHorizontalHeaderItem(4, QTableWidgetItem("E-mail ID"))
        self.table_viewUnknownDetails.setHorizontalHeaderItem(5, QTableWidgetItem("D.O.B"))
        self.cursor.execute('SELECT * FROM rtmfr.person_data WHERE person_isRecognized=0')
        for row, form in enumerate(self.cursor):
            # self.table_viewDetails.insertRow(row)
            for column, item in enumerate(form):
                    self.table_viewUnknownDetails.setItem(row, column, QTableWidgetItem(str(item)))

class BlockDetails(QWidget):
    mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
    cursor = mydb.cursor()

    def __init__(self, parent):
        super(BlockDetails, self).__init__(parent)

        layout = QVBoxLayout()

        self.table_viewDetails = QTableWidget()
        layout.addWidget(self.table_viewDetails)


        self.button_refresh = QPushButton("Refresh")
        layout.addWidget(self.button_refresh)

        self.button_refresh.clicked.connect(lambda : self.loadTable())

        self.setLayout(layout)

    def loadTable(self):
        self.cursor.execute('SELECT COUNT(*) FROM rtmfr.person_data WHERE person_isBlacklisted=1')
        rowcount = self.cursor.fetchall()
        print(rowcount[0][0])
        self.table_viewDetails.setRowCount(rowcount[0][0])
        self.table_viewDetails.setColumnCount(6)

        self.table_viewDetails.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table_viewDetails.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table_viewDetails.setHorizontalHeaderItem(2, QTableWidgetItem("Designation"))
        self.table_viewDetails.setHorizontalHeaderItem(3, QTableWidgetItem("Mobile Number"))
        self.table_viewDetails.setHorizontalHeaderItem(4, QTableWidgetItem("E-mail ID"))
        self.table_viewDetails.setHorizontalHeaderItem(5, QTableWidgetItem("D.O.B"))

        self.cursor.execute('SELECT * FROM rtmfr.person_data WHERE person_isBlacklisted=1')
        for row, form in enumerate(self.cursor):
            # self.table_viewDetails.insertRow(row)
            for column, item in enumerate(form):
                    self.table_viewDetails.setItem(row, column, QTableWidgetItem(str(item)))
