from tkinter import *
from tkinter import ttk

class One:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("850x300+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')


        label = Label(root, text="Facial recognition is a way of identifying or confirming an individual’s identity using their face.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10,y=30)

        label1 = Label(root, text="Facial recognition systems can be used to identify people in photos, videos, or in real-time.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label1.place(x=10, y=55)

        label2 = Label(root, text="Facial recognition is a category of biometric security. Other forms of biometric software", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label2.place(x=10, y=110)

        label3 = Label(root, text="include voice recognition, fingerprint recognition, and eye retina or iris recognition. ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label3.place(x=10, y=140)

        label4 = Label(root, text="The technology is mostly used for security and law enforcement, though there is increasing", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label4.place(x=10, y=170)

        label5 = Label(root, text="interest in other areas of use.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label5.place(x=10, y=200)



if __name__ == "__main__":
    root = Tk()
    obj = One(root)
    root.mainloop()