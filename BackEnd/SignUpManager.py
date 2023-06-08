import mysql.connector


class SignUpManager(object):
    mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
    cursor = mydb.cursor()


    def addOperator(self,operator_Id,operator_name,operator_Mobile_No,operator_Email_Id,operator_Cus_Id ,operator_Password,operator_Conform_Password):
        self.cursor.execute("SELECT op_Id FROM rtmfr.operator_data WHERE op_Id ="+str(operator_Id))
        resultSet = self.cursor.fetchone()

        if resultSet is not None:
            return -1


        sqlQuery = "INSERT INTO operator_data (`op_Id`, `op_Name`, `op_Mobile`, `op_Email_Id`, `op_Cus_Id`, `op_Pass`) VALUES(%s,%s,%s,%s,%s,%s)"


        if (operator_Password == operator_Conform_Password):
            operator = (operator_Id, operator_name, operator_Mobile_No, operator_Email_Id, operator_Cus_Id , operator_Password)
            self.cursor.execute(sqlQuery, operator)
            self.mydb.commit()
            return 0
        else:
            return -2
