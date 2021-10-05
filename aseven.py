from tkinter import *
from tkinter import ttk

class Seven:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("870x300+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label = Label(root, text="A time and attendance system using facial recognition technology can accurately report attendance,", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=30)

        label = Label(root, text="absence, and overtime with an identification process that is fast as well as accurate.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=60)

        label = Label(root, text="Labor cost savings:", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=10, y=100)

        label = Label(root, text="Facial recognition software can accurately track time and attendance without human error.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=40, y=130)

        label = Label(root, text="It keeps track of the exact number of hours an employee is working, which can help save the", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=40, y=160)

        label = Label(root, text="company money. You will never have to worry about time fraud or “buddy punching” with a facial", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=40, y=190)

        label = Label(root, text="recognition time tracking system.", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label.place(x=40, y=220)


if __name__ == '__main__':
    root = Tk()
    obj = Seven(root)
    root.mainloop()
