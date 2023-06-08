import cv2
import mysql.connector
import re


def check(email):
    if (re.search(regex, email)):
        person = (
        person_Id, person_name, person_Designation, person_Mobile_No, person_Email_Id, person_DOB, person_Aadhar_No)
        cursor.execute(sqlQuery, person)
        mydb.commit()
        print(cursor.rowcount, "You are Registered ")
    else:
        print("Invalid Email")


mydb = mysql.connector.connect(host="localhost",user="root",password="186490316018",database="rtmfr")
cursor = mydb.cursor()

sqlQuery = "INSERT INTO person_data VALUES(%s,%s,%s,%s,%s,%s,%s)"

print("Enter your id:")
person_Id = 6019 #input()

print("Enter your Name:")
person_name = 'Bhavanshu Dalwadi' #input()

print("Enter your Designation:")
person_Designation= 'Student' #input()

print("Enter your Mobile Number:")
person_Mobile_No = '7048723383' #input()

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
print("Enter your E-mail Id:")
person_Email_Id = 'bhavanshu.dalwadi@gmail.com' #input()

print("Enter your DOB:")
person_DOB ='2002-08-11' # input()

print("Enter your Aadhar Number:")
person_Aadhar_No= '123412341235' #input()

check(person_Email_Id)

cam = cv2.VideoCapture(0)
cam.set(3, 640)     #Width
cam.set(4, 480)     #Height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = person_Id
num_of_images = 0
print('\n [RMFTR_SYS_INFO] Initializing face capture for Real Time Multi Face Recognition.')


count = 0

while True:
    ret, img = cam.read()   #Web cam currently
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Converting images in gray color

    faces = face_detector.detectMultiScale(gray,1.3,5)
    #1.3 to 5 is the standard dimension

    for(x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
        count += 1
        cv2.putText(img, str(str(num_of_images) + " images captured"), (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 0, 255))
        cv2.imwrite('dataset/Student.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y + h, x:x +w])

        cv2.imshow('image',img)

    #Time to wait till it is stored in dataset
    k = cv2.waitKey(10) & 0xff


    if k == 27:
        break
    elif count >= 300:   #Terminates when no. images = count
        break

#cleanup
print("\n [INFO] Exiting Real Time Multi Face Recognition")
cam.release()
cv2.destroyAllWindows()




