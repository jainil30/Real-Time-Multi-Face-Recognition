import mysql.connector

class LoginManager(object):
    mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
    cursor = mydb.cursor()

    def checkLoginCredentials(self,id,password):
        operator_id = id
        operator_Password = password

        try:
            sqlQuery = "SELECT * FROM operator_data WHERE op_Id=%s AND op_Pass=%s"
            credentials = (operator_id,operator_Password)
            self.cursor.execute(sqlQuery, credentials)
            result = self.cursor.fetchone()
            print(result)
            if result is None:
                return -2
            else:
                return result
        except:
            print("Error!!")
            return -2

