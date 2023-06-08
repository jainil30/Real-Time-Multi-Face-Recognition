import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
cursor  = mydb.cursor()

id = 6018
sqlQuery = ("SELECT person_Name FROM person_data WHERE person_Id=" + str(id))
cursor.execute(sqlQuery)
result = cursor.fetchone()
data = []
for row in result:
    data.append(row)
for name in data:
    print('Names : ', name)






