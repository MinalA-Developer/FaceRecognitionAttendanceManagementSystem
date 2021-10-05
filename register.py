from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
import webbrowser as wb

class Register:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Registration")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # background Image

        bg = Image.open(r"Images/GSK_headerimage_1280x720.png")
        bg = bg.resize((1350, 690), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=250, y=0, width=1350, height=690)

        # Left Image
        left_img = Image.open(r"Images/leftimg.png")
        left_img = left_img.resize((400, 500), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(left_img)

        bg_img1 = Label(self.root, image=self.photoimg2)
        bg_img1.place(x=80, y=100, width=400, height=500)

        # Register Frame
        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=480, y=100, width=700, height=500)

        title = Label(Frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="#0066b2").place(x=50, y=30)

        # First Name
        f_name = Label(Frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(Frame1, font=("time new roman",15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(Frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(Frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact Number
        Contact_no = Label(Frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(Frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        l_email = Label(Frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(Frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        question = Label(Frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.cmb_question = ttk.Combobox(Frame1, font=("times new roman", 13), state="readonly")
        self.cmb_question["values"]=("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_question.current(0)
        self.cmb_question.place(x=50, y=270, width=250)

        # answer
        answer = Label(Frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(Frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # password
        password = Label(Frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(Frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        # Confirm Password
        con_password = Label(Frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_con_password = Entry(Frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_con_password.place(x=370, y=340, width=250)

        # checkbox
        self.var_chk = IntVar()
        chk = Checkbutton(Frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, font=("times new roman", 12, "bold"), bg="white").place(x=50, y=380)

        # Register Button
        # self.btn_image = ImageTk.PhotoImage(file=r"Images/Register-Now-Button-Green.jpg")
        # btn_register = Button(Frame1, image=self.btn_image, bd=0, cursor="hand2", height=70).place(x=50, y=420)

        self.btn_register = Button(Frame1, text="Register Now", cursor="hand2", command=self.register_data, font=("times new roman", 20, "bold"), bd=0, bg="#6699CC", fg="black").place(x=50, y=420)

        self.btn_instructions = Button(Frame1, text="instructions", cursor="hand2", command=self.openPdf, font=("times new roman", 20, "bold"), bd=0, bg="white", fg="black").place(x=370, y=420)

        btn_sign_in = Button(bg_img1, text="Sign In", cursor="hand2", command=self.callNewScreen, font=("times new roman", 20), bd=0).place(x=110, y=320, width=160)


    def openPdf(self):
        wb.open_new(r'G:\Python\FaceRecognitionProject\Instructions.pdf')

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_con_password.delete(0, END)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_con_password.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.txt_password.get()!=self.txt_con_password.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree our terms and Conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                # my_cursor.execute("select * from register where email=%s", self.txt_email.get())
                # row = my_cursor.fetchone()
                # print(row)
                my_cursor.execute("insert into register(f_name,l_name,contact,email,question,answer,password) values(%s, %s, %s, %s, %s, %s, %s)",
                                      (self.txt_fname.get(),
                                       self.txt_lname.get(),
                                       self.txt_contact.get(),
                                       self.txt_email.get(),
                                       self.cmb_question.get(),
                                       self.txt_answer.get(),
                                       self.txt_password.get()
                                      ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
                self.clear()
                root.destroy()
                os.system('login.py')
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def callNewScreen(self):
        root.destroy()
        os.system('login.py')






if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
