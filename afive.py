from tkinter import *
from tkinter import ttk

class Five:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("870x670+200+20")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label = Label(root, text="Aside from unlocking your smartphone, facial recognition brings other benefits to the companies.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=10)

        label1 = Label(root, text="# Enhanced security", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label1.place(x=10, y=55)

        label2 = Label(root, text="The first thing to start with is surveillance. With the help of facial recognition, it will be easier to", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label2.place(x=40, y=90)

        label3 = Label(root, text="track down any burglars, thieves, or other trespassers.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label3.place(x=40, y=120)

        label4 = Label(root, text="On a governmental level, facial recognition can help to identify terrorists or other criminals.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label4.place(x=40, y=170)

        label5 = Label(root, text="On a personal level, facial recognition can be used as a security tool for locking personal devices", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label5.place(x=40, y=200)

        label6 = Label(root, text="and for personal surveillance cameras.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label6.place(x=40, y=230)

        label7 = Label(root, text="# Faster processing", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label7.place(x=10, y=270)

        label8 = Label(root, text="The process of recognizing a face takes a second or less - and this is incredibly beneficial for the", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label8.place(x=40, y=305)

        label9 = Label(root, text="companies. In the era of constant cyber attacks and advanced hacking tools, companies need a", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label9.place(x=40, y=335)

        label10 = Label(root, text="technology that would be both secure and fast. Facial recognition enables quick and efficient", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label10.place(x=40, y=365)

        label11 = Label(root, text="verification of a person’s identity.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label11.place(x=40, y=395)

        label12 = Label(root, text="# Seamless integration", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label12.place(x=10, y=445)

        label13 = Label(root, text="This is probably one of the biggest benefits for companies. The facial recognition technology is", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label13.place(x=40, y=480)

        label14 = Label(root, text="quite easily integrated so it’s a perfect choice.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label14.place(x=40, y=510)

        label15 = Label(root, text="# Automation of identification", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label15.place(x=10, y=560)

        label16 = Label(root, text="Before, security guards had to perform manual identification of a person that took too much time", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label16.place(x=40, y=590)

        label17 = Label(root, text="and did not boast high accuracy.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label17.place(x=40, y=620)







if __name__ == "__main__":
    root = Tk()
    obj = Five(root)
    root.mainloop()
