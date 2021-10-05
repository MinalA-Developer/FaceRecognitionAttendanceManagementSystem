from tkinter import*
import tkinter.messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os
from employee import Employee
from train import Train
from face_recognition import Face_Recognition
from developer import Contact
from FAQ import Faq
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        # First Image
        img = Image.open(r"G:\Python\FaceRecognitionProject\Images\1.jpg")
        img = img.resize((460,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=460, height=130)

        # Second Image
        img1 = Image.open(r"G:\Python\FaceRecognitionProject\Images\facialrecognition.png")
        img1 = img1.resize((460, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=460, y=0, width=460, height=130)

        # Third Image
        img2 = Image.open(r"G:\Python\FaceRecognitionProject\Images\3.jpg")
        img2 = img2.resize((460, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=920, y=0, width=460, height=130)

        # Background Image

        img3 = Image.open(r"Images\abstract-technology-background-hi-tech-communication-concept-innovation_42421-384.jpg")
        img3 = img3.resize((1350, 690), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1350, height=690)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        # Employee Button
        img4 = Image.open(r"Images\employees.jpg")
        img4 = img4.resize((160, 160), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.employee_details, cursor="hand2")
        b1.place(x=100, y=90, width=160, height=160)

        b1_1 = Button(bg_img, text="Employee Details", command=self.employee_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=250, width=160, height=40)

        # Detect Face Button
        img5 = Image.open(r"Images\facial-recognition-feature_1200x675_hero_090418.jpg")
        img5 = img5.resize((160, 160), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.Face_Data)
        b1.place(x=400, y=90, width=160, height=160)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.Face_Data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=250, width=160, height=40)

        # Attendance Button
        img6 = Image.open(r"Images\attendance-clipart-time-card-18.png")
        img6 = img6.resize((160, 160), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.Attendace)
        b1.place(x=700, y=90, width=160, height=160)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.Attendace, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700, y=250, width=160, height=40)

        # FAQ Button
        img7 = Image.open(r"Images\Faq.jpg")
        img7 = img7.resize((160, 160), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.Faq)
        b1.place(x=1000, y=90, width=160, height=160)

        b1_1 = Button(bg_img, text="FAQ", cursor="hand2", command=self.Faq, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=250, width=160, height=40)

        # Train Data Button
        img8 = Image.open(r"G:\Python\FaceRecognitionProject\Images\c.jpg")
        img8 = img8.resize((160, 160), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.Train_data)
        b1.place(x=100, y=330, width=160, height=160)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.Train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=490, width=160, height=40)

        # Photos Button
        img9 = Image.open(r"Images\face-detection.png")
        img9 = img9.resize((160, 160), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=330, width=160, height=160)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=490, width=160, height=40)

        # Contact Button
        img10 = Image.open(r"Images\contactus.jpg")
        img10 = img10.resize((160, 160), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.Contact)
        b1.place(x=700, y=330, width=160, height=160)

        b1_1 = Button(bg_img, text="Contact Us", cursor="hand2", command=self.Contact, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700, y=490, width=160, height=40)

        # Exit Button
        img11 = Image.open(r"Images\depositphotos_26329725-stock-photo-exit-circle-blue-glossy-icon.jpg")
        img11 = img11.resize((160, 160), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1000, y=330, width=160, height=160)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000, y=490, width=160, height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project", parent = self.root)

        if self.iExit >0:
            self.root.destroy()
        else:
            return

    # ===============Functions Button==============

    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Employee(self.new_window)

    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def Face_Data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Faq(self):
        self.new_window=Toplevel(self.root)
        self.app = Faq(self.new_window)

    def Contact(self):
        self.new_window=Toplevel(self.root)
        self.app = Contact(self.new_window)

    def Attendace(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
