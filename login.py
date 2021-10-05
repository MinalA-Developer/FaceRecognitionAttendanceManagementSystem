import os
from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        # bg image

        bg = Image.open(r"Images/b-slide11.jpg")
        bg = bg.resize((1350,690), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1350, height=690)

        frame1 = Frame(self.root, bg="#eef2f3")
        frame1.place(x=400, y=150, width=600, height=400)

        title = Label(frame1, text="Login Here", font=("times new roman", 35, "bold"), bg="#eef2f3", fg="#318CE7").place(x=80, y=30)

        # Email
        lable_email = Label(frame1, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="#eef2f3", fg="gray").place(x=80, y=120)
        self.txt_email_address = ttk.Entry(frame1, font=("times new roman", 18))
        self.txt_email_address.place(x=80, y=150, width=350)

        # Password
        lable_password = Label(frame1, text="PASSWORD", font=("times new roman", 18,"bold"), bg="#eef2f3", fg="gray").place(x=80, y=200)
        self.txt_password = ttk.Entry(frame1, show="*   ", font=("times new roman", 18))
        self.txt_password.place(x=80, y=230, width=350)

        btn_register = Button(frame1, text="Register New Account?", command=self.callRegister, font=("times new roman", 14), bg="#eef2f3", fg="#318CE7", bd=0).place(x=80, y=270)

        btn_forget_password = Button(frame1, text="Forget Password?", command=self.forget_password_window, font=("times new roman", 14), bg="#eef2f3", fg="#318CE7", bd=0).place(x=300, y=270)

        btn_login = Button(frame1, text="Login", command=self.login, font=("times new roman", 20), fg="#eef2f3", bg="#318CE7").place(x=80, y=310, width=180, height=40)


    # Functions

    def reset(self):
        self.cmb_question.current(0)
        self.txt_answer.delete(0, END)
        self.txt_new_password.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_email_address.delete(0, END)

    def forget_password(self):
        if self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s and question=%s and answer=%s", (self.txt_email_address.get(), self.cmb_question.get(), self.txt_answer.get()))
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select the correct Security Question / Enter Correct Answer", parent=self.root2)
                else:
                    my_cursor.execute("update register set password=%s where email=%s",(self.txt_new_password.get(), self.txt_email_address.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your Password has been reset successfully, Please Login with new Password", parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root2)

    def forget_password_window(self):
        if self.txt_email_address.get()=="":
            messagebox.showerror("Error", "Please enter the valid email address to reset your password", parent=self.root)
        else:
            self.root2 = Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("360x400+480+200")
            self.root2.config(bg="#eef2f3")
            self.root2.focus_force()
            self.root2.resizable(False, False)
            self.root2.grab_set()

            title = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="#eef2f3", fg="#002D62").place(x=80, y=10)

            # Security Question
            question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="gray").place(x=50, y=80)

            self.cmb_question = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly")
            self.cmb_question["values"] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
            self.cmb_question.current(0)
            self.cmb_question.place(x=50, y=110, width=250)

            # answer
            answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="gray").place(x=50, y=160)
            self.txt_answer = ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_answer.place(x=50, y=190, width=250)

            # new password
            new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="#eef2f3", fg="gray").place( x=50, y=240)
            self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_new_password.place(x=50, y=270, width=250)

            # Button
            Change_Password = Button(self.root2, text="Reset Password", command=self.forget_password, font=("times new roman", 20), fg="#eef2f3", bg="#002D62").place(x=80, y=320, width=190, height=40)


    def login(self):
        if self.txt_email_address.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Warning", "All fields are required!!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s", (self.txt_email_address.get(), self.txt_password.get()))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    conn.close()
                    root.destroy()
                    os.system('main.py')
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def callRegister(self):
        root.destroy()
        os.system('register.py')










if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()