from tkinter import *
from tkinter import ttk

class Four:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("870x470+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label = Label(root, text="Face recognition systems capture an incoming image from a camera device in a two-dimensional or ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=30)

        label1 = Label(root, text="three-dimensional way depending on the characteristics of the device. ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label1.place(x=10, y=55)

        label2 = Label(root, text="These ones compare the relevant information of the incoming image signal in real-time in photo or", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label2.place(x=10, y=110)

        label3 = Label(root, text="video in a database, being much more reliable and secure than the information obtained in a static", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label3.place(x=10, y=140)

        label4 = Label(root, text="image. This biometric facial recognition procedure requires an internet connection since the database", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label4.place(x=10, y=170)

        label5 = Label(root, text="cannot be located on the capture device as it is hosted on servers.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label5.place(x=10, y=200)

        label6 = Label(root, text="Facial technology systems can vary, but in general, they tend to operate as follows:", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label6.place(x=10, y=255)

        label7 = Label(self.root, text="Step One : ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label7.place(x=10, y=290)

        label8 = Label(root, text="Face detection", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label8.place(x=110, y=290)

        label9 = Label(self.root, text="Step Two : ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label9.place(x=10, y=330)

        label10 = Label(root, text="Face analysis", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label10.place(x=110, y=330)

        label11 = Label(self.root, text="Step Three : ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label11.place(x=10, y=370)

        label12 = Label(root, text="Converting the image to data", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label12.place(x=125, y=370)

        label11 = Label(self.root, text="Step Four : ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label11.place(x=10, y=410)

        label12 = Label(root, text="Finding a match", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label12.place(x=110, y=410)


if __name__ == "__main__":
    root = Tk()
    obj = Four(root)
    root.mainloop()