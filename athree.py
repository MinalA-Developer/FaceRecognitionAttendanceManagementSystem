from tkinter import *
from tkinter import ttk

class Three:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("850x300+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label1 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label1.place(x=10, y=10)

        label2 = Label(root, text="Unlocking phones", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label2.place(x=35, y=25)

        label3 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label3.place(x=10, y=45)

        label4 = Label(root, text="Law enforcement", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label4.place(x=35, y=60)

        label5 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label5.place(x=10, y=80)

        label6 = Label(root, text="Airports and border control", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label6.place(x=35, y=95)

        label7 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label7.place(x=10, y=115)

        label8 = Label(root, text="Finding missing persons", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label8.place(x=35, y=130)

        label9 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label9.place(x=10, y=150)

        label10 = Label(root, text="Reducing retail crime", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label10.place(x=35, y=165)

        label11 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label11.place(x=10, y=185)

        label12 = Label(root, text="Improving retail experiences", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label12.place(x=35, y=200)

        label13 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label13.place(x=400, y=10)

        label14 = Label(root, text="Banking", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label14.place(x=425, y=25)

        label15 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label15.place(x=400, y=45)

        label16 = Label(root, text="Marketing and advertising", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label16.place(x=425, y=60)

        label17 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label17.place(x=400, y=80)

        label18 = Label(root, text="Healthcare", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label18.place(x=425, y=95)

        label17 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label17.place(x=400, y=115)

        label18 = Label(root, text="Tracking student or worker attendance", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label18.place(x=425, y=130)

        label19 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label19.place(x=400, y=150)

        label20 = Label(root, text="Recognizing drivers", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label20.place(x=425, y=165)

        label19 = Label(self.root, text="-", font=("times new roman", 30, "bold"), bg="#eef2f3", fg="#002244")
        label19.place(x=400, y=185)

        label20 = Label(root, text="Monitoring gambling addictions", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label20.place(x=425, y=200)









if __name__ == "__main__":
    root = Tk()
    obj = Three(root)
    root.mainloop()