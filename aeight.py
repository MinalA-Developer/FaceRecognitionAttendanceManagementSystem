from tkinter import *
from tkinter import ttk

class Eight:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("870x250+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label = Label(root, text="The performance of a face recognition system depends on the quality of both test and reference", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=50)

        label = Label(root, text="images participating in the face comparison process. The accuracy of the system is depends on the", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=80)

        label = Label(root, text="quality of the image taken. This accuracy is also impacted by lighting - poorly lit image may fill to be", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=110)

        label = Label(root, text="rocognised. Recognition is generally achieved in 2-3 clear images taken in the same location.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=140)


if __name__ == '__main__':
    root = Tk()
    obj = Eight(root)
    root.mainloop()
