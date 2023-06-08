import mysql.connector
import re
from datetime import datetime

class AddPersonDetails(object):
    mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018")
    cursor = mydb.cursor()
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    def addPersonDetails(self,person_Id,person_name,person_Designation,person_Mobile_No,person_Email_Id,person_DOB,person_Aadhar_No):
        self.cursor.execute("SELECT person_Id FROM rtmfr.person_data WHERE person_Id ="+str(person_Id))
        resultSet = self.cursor.fetchone()

        if resultSet is not None:
            return -1

        sqlQuery = "INSERT INTO rtmfr.person_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        print("In addPersonDetails")
        if (re.search(self.regex,person_Email_Id)):
            person = (person_Id,person_name,person_Designation, person_Mobile_No, person_Email_Id, person_DOB, person_Aadhar_No,0,0)
            #person = ( 99, "Abc", "STD", 9089, "soham@as.com", "1992-06-22", 12213, 0,0 )
            self.cursor.execute(sqlQuery, person)
            self.mydb.commit()
            return 0
        else:
            print("Invalid Email")
            return -2






