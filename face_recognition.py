from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Face Detector")
        self.root.resizable(False, False)

        # Title
        title_label = Label(self.root, text="FACE RECOGNITION", font=("algerian", 35, "bold"), bg="white", fg="blue")
        title_label.place(x=0, y=0, width=1350, height=45)

        # Left Image
        img1 = Image.open(r"Images/1622790494289.jpg")
        img1 = img1.resize((650, 610), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=0, y=45, width=650, height=610)

        # Right Image
        img2 = Image.open(r"Images/a.jpg")
        img2 = img2.resize((700, 610), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        img_lbl1 = Label(self.root, image=self.photoimg3)
        img_lbl1.place(x=650, y=45, width=700, height=610)

        # Button
        btn = Button(img_lbl1, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        btn.place(x=250, y=535, width=200, height=40)

        # down Title
        title_label1 = Label(self.root, text="Frontal Face Detector", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_label1.place(x=0, y=650, width=1350, height=45)

    # ==================attendance=================
    def mark_attendance(self,i,n,d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1}, Present")



    # ====================Face Recognition======================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from employee where Emp_id="+str(id))
                n = my_cursor.fetchone()
                # print(n, type(n))
                n="+".join(n)

                my_cursor.execute("select Dep from employee where Emp_id="+str(id))
                d = my_cursor.fetchone()
                # print(d, type(d))
                d="+".join(d)

                my_cursor.execute("select Emp_id from employee where Emp_id=" + str(id))
                i = my_cursor.fetchone()
                # print(d, type(d))
                i = "+".join(i)

                if confidence>77:
                    cv2.putText(img, f"Employee ID:{i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department:{d}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0,0,255), 3)
                    cv2.putText(img,"Unknown Face", (x,y-30), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord

        def recognize(img, clf, faceCascade):
            coord=draw_boundray(img, faceCascade,1.1,10,(255,255,255), "Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        address = "http://192.168.0.102:8080//video"
        video_cap.open(address)

        while True:
            ret, img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
