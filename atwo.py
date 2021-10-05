from tkinter import *
from tkinter import ttk

class Two:
    def __init__(self, root):
        self.root = root
        self.root.title("Answer")
        self.root.geometry("850x250+200+100")
        self.root.resizable(False, False)
        self.root.config(bg='#eef2f3')

        label1 = Label(self.root, text="The accuracy rate is up to 99%, but accuracy depends on the quality of the image taken. A series", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label1.place(x=10,y=40)

        label2 = Label(root, text="of images are required to train the engine for each individual user, and a variety of different angles", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label2.place(x=10, y=70)

        label3 = Label(root, text="help us to reach higher image recognition accuracy. This accuracy is also impacted by lighting – a", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label3.place(x=10, y=100)

        label4 = Label(root, text="poorly lit image may fail to be recognised. Recognition is generally achieved in 2-3 clear images", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label4.place(x=10, y=130)

        label5 = Label(root, text="taken in the same location. If the camera location varies, we recommend up to 10 images to achieve highest accuracy. ", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="#002244")
        label5.place(x=10, y=160)





if __name__ == "__main__":
    root = Tk()
    obj = Two(root)
    root.mainloop()