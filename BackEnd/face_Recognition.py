import cv2
from datetime import datetime
import mysql.connector
import csv

mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
cursor  = mydb.cursor()

#LBPH  algo. for face recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_TRIPLEX

#id = 0
#names = ["Papa","Jainil Dalwadi","Deep Mangukiya"]

#Web Cam currently
cam = cv2.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)

mimWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)

def markAttendance(id,name):
    with open('Attendance.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name"])
        insert = [id, name]
        writer.writerow(insert)


 #   with open('Attendance.csv', 'w+') as f:
      #  myDataList = f.readlines()
  #      myDataList = []
#        nameList = []
 #       for line in myDataList:
  #          entry = line.split(',')
   #         nameList.append(entry[0])
    #        if name not in nameList:
     #           now = datetime.now()
      #          dt_string = now.strftime('%H:%M:%S')
       #         f.writelines(f'\n{name},{dt_string}')


while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=2,     #Depends on other enity except the current in frame
        minSize=(int(mimWidth),int(minHeight))
    )

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        no = 0
        print(id)

        if (confidence < 100):
            no = id
            print(id)
           # id = names[id]
            sqlQuery = ("SELECT person_Name FROM person_data WHERE person_Id=" + str(id))
            cursor.execute(sqlQuery)
            result = cursor.fetchone()
            data = []
            for row in result:
                data.append(row)
            for name in data:
                print('Names : ', name)
            confidence = " {0}%".format(round(100-confidence))
        else:
            id = "You are Unauthorized! Wait for the guards"
            confidence ="{0}%".format((round(100-confidence)))
        cv2.putText(img, name, (x+5, y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255,255,0), 1)
        markAttendance(str(id),name)
       # updatedb(no,names[no])

    cv2.imshow('Web Cam', img)

    k = cv2.waitKey(10) & 0xff
    #Currently not working properly
    if k == 27:
        break

print("\n [INFO] Closing Real Time Multi Face Recognition")
cam.release()
cv2.destroyAllWindows()








