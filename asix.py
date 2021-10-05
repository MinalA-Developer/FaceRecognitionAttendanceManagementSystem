from tkinter import *
from tkinter import ttk

class Six:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("850x200+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label = Label(root, text="Yes – the facial recognition engine uses the various angles and points of your face to verify your", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=50)

        label = Label(root, text="identity and after it has been trained to recognise you, it will be able to identify you with a variety", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=80)

        label = Label(root, text="of different looks!", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=110)


if __name__ == '__main__':
    root = Tk()
    obj = Six(root)
    root.mainloop()
