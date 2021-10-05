from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Train Data")
        self.root.resizable(False, False)

        # Variables
        self.var_checkbox= IntVar()

        # background Image
        bg = Image.open(r"Images/bgimg.jpg")
        bg = bg.resize((1350,690), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1350, height=690)

        # Title
        title_label = Label(bg_img, text="TRAIN DATA SET", font=("algerian", 35, "bold"), bg="white", fg="red")
        title_label.place(x=0, y=0, width=1350, height=45)

        # Image
        img1 = Image.open(r"Images/Face-recognition-technology.png")
        img1 = img1.resize((650,280), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        img_lbl = Label(bg_img, image=self.photoimg2)
        img_lbl.place(x=350, y=80, width=650, height=280)

        # CheckBox Sentence
        Check_box = Checkbutton(bg_img, text="Do you Want to See the Sample while training the System", onvalue=1, offvalue=0, font=("times new roman", 17, "bold"), variable=self.var_checkbox)
        Check_box.place(x=360, y=385)
        # Sen_label = Label(bg_img, , font=("times new roman", 18, "bold"))
        # Sen_label.place(x=400, y=380)

        # Train Button
        train_btn = Button(bg_img, text="Start Training", command = self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="yellow", fg="black")
        train_btn.place(x=580, y=440,  width=200, height=60)

        # Progress Bar
        self.bar = ttk.Progressbar(bg_img, length=500, orient=HORIZONTAL)
        self.bar.place(x=380, y=520)

    # Functions
    def train_classifier(self):
        if self.var_checkbox.get()==1:
            data_dir = ("data")
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')    # Gray Scale image
                imageNp = np.array(img, 'uint8')        # Uint is datatypes in array
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Train Data", imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            # ====================== Train The Classifier And Save ======================
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Train Dataset Completed!!!", parent=self.root)

        else:
            task = 10
            x = 0
            while(x<task):
                time.sleep(1)
                self.bar['value']+=10
                x+=1
                self.root.update_idletasks()
            data_dir = ("data")
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')  # Gray Scale image
                imageNp = np.array(img, 'uint8')  # Uint is datatypes in array
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                # cv2.imshow("Train Data", imageNp)
                # cv2.waitKey(1) == 13
            ids = np.array(ids)

            # ====================== Train The Classifier And Save ======================
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Train Dataset Completed!!!", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
