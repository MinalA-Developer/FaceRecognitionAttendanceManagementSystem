import os
from tkinter import *
from tkinter import ttk
import pywhatkit as kit


class Faq:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ")
        self.root.geometry("1350x690+0+0")
        self.root.resizable(False, False)
        self.root.config(bg='#08AEEA')


        frame = Frame(self.root, bd=2, relief=RAISED, bg='#eef2f3')
        frame.place(x=250, y=40, width=900, height=600)

        title_label = Label(frame, text="FAQ", font=("times new roman", 35, "bold"), bg="#eef2f3", fg="#8B0000")
        title_label.place(x=400, y=0)
        # 004526

        btn_1 = Button(frame, text="What is face recognition?", command=self.One, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=110)

        btn_2 = Button(frame, text="How accurate is it?", command=self.Two, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=150)

        btn_3 = Button(frame, text="How facial recognition used for?", command=self.Three, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=190)

        btn_4 = Button(frame, text="How does the face recognition attendance system work?", command=self.Four, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=230)

        btn_5 = Button(frame, text="What are the benefits of the face recognition?", command=self.Five, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=270)

        btn_6 = Button(frame, text="Will I be recognised with glasses / a beard / a new haircut?", command=self.Six, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=310)

        btn_7 = Button(frame, text="Why do we need face recognition attendance system?", command=self.Seven, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=350)

        btn_8 = Button(frame, text="Does the quality of the photos impact on the attendance?", command=self.Eight, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=390)

        btn_9 = Button(frame, text="Where can I find more information on Face recognition?", command=self.Nine, font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=430)

        # btn_10 = Button(frame, text="Which technique is used for this system?", font=("times new roman", 20), bg="#eef2f3", fg="#0a2351", bd=0).place(x=80, y=470)

    # functions
    def One(self):
        os.system('aone.py')

    def Two(self):
        os.system('atwo.py')

    def Three(self):
        os.system('athree.py')

    def Four(self):
        os.system('afour.py')

    def Five(self):
        os.system('afive.py')

    def Six(self):
        os.system('asix.py')

    def Seven(self):
        os.system('aseven.py')

    def Eight(self):
        os.system('aeight.py')

    def Nine(self):
        kit.playonyt("what is face recognition and how its work")










if __name__ == "__main__":
    root = Tk()
    obj = Faq(root)
    root.mainloop()