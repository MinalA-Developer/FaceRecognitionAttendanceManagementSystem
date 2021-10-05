from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Contact:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Contact Us")
        self.root.resizable(False, False)
        self.root.config(bg='#274046')

        # Title
        title_label = Label(self.root, text="CONTACT US", font=("algerian", 35, "bold"), fg="#FFC72C", bg='#274046')
        title_label.place(x=0, y=30, width=1350, height=45)

        title_label = Label(self.root, text="_______", font=("algerian", 35, "bold"), fg="#FFC72C", bg='#274046')
        title_label.place(x=0, y=70, width=1350, height=45)

        title_label = Label(self.root, text="We align leaders around a shared purpose and strategic story that catalyzes their", font=("Times New Roman", 15, "bold"), fg="white", bg='#274046')
        title_label.place(x=0, y=120, width=1350, height=45)

        title_label1 = Label(self.root, text="business and brand to take action", font=("Times New Roman", 15, "bold"), fg="white", bg='#274046')
        title_label1.place(x=20, y=155, width=1350, height=45)

        # Image
        img1 = Image.open(r"Images/map.jpg")
        img1 = img1.resize((1350, 340), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=0, y=350, width=1350, height=340)

        # Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=50, y=220, width=1250, height=270)

        # Image
        img2 = Image.open(r"Images/Address.png")
        img2 = img2.resize((80, 80), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        img_lbl = Label(main_frame, image=self.photoimg3)
        img_lbl.place(x=170, y=30, width=80, height=80)

        # Image
        img3 = Image.open(r"Images/Email.png")
        img3 = img3.resize((80, 80), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img3)

        img_lbl = Label(main_frame, image=self.photoimg4)
        img_lbl.place(x=570, y=30, width=80, height=80)

        # Image
        img4 = Image.open(r"Images/Call.png")
        img4 = img4.resize((80, 80), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img4)

        img_lbl = Label(main_frame, image=self.photoimg5)
        img_lbl.place(x=970, y=30, width=80, height=80)

        # Address
        Add_label = Label(main_frame, text="Address:", font=("times new roman", 16, "bold"), bg="white", fg="gray")
        Add_label.place(x=170, y=120)

        Add_label1 = Label(main_frame, text="M. J. Phule Road, Naigaon,", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        Add_label1.place(x=110, y=160)

        Add_label2 = Label(main_frame, text="Dadar (E), Mum 400014", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        Add_label2.place(x=120, y=190)

        # Email
        email_label = Label(main_frame, text="Email:", font=("times new roman", 16, "bold"), bg="white", fg="gray")
        email_label.place(x=580, y=120)

        email_label1 = Label(main_frame, text="hello@company.com", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        email_label1.place(x=530, y=160)

        email_label2 = Label(main_frame, text="support@company.com", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        email_label2.place(x=520, y=190)

        # Contact
        email_label = Label(main_frame, text="Call us:", font=("times new roman", 16, "bold"), bg="white", fg="gray")
        email_label.place(x=970, y=120)

        email_label1 = Label(main_frame, text="+91 8591297003", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        email_label1.place(x=940, y=160)

        email_label2 = Label(main_frame, text="+91 8692850821", font=("times new roman", 13, "bold"), bg="white", fg="gray")
        email_label2.place(x=940, y=190)






if __name__ == "__main__":
    root = Tk()
    obj = Contact(root)
    root.mainloop()