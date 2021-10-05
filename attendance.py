from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Attendance")
        self.root.config(bg='#81D8D0')
        self.root.resizable(False, False)
        # background - color:  # 85FFBD;
        # background - image: linear - gradient(45
        # deg,  #85FFBD 0%, #FFFB7D 100%);

        # ===============Variables===============
        self.var_atten_id = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_attendance = StringVar()


        # First Image
        img = Image.open(r"Images\face-detection.png")
        img = img.resize((675, 170), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=675, height=170)

        # Second Image
        img1 = Image.open(r"Images\employeeretention.png")
        img1 = img1.resize((675, 170), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=675, y=0, width=675, height=170)

        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="#1E2952")     #002244
        title_lbl.place(x=0, y=170, width=1350, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=220, width=1320, height=465)

        # Left Label Frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Record", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=5, width=640, height=450)

        img_left = Image.open(r"Images\FaceDetector.jpg")
        img_left = img_left.resize((620, 135), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_Frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=620, height=135)

        # Attendance Record Frame
        Attendance_Frame = Frame(Left_Frame, bd=2, bg="white", relief=RIDGE)
        Attendance_Frame.place(x=5, y=140, width=630, height=285)

        # ID Label
        Id_Label = Label(Attendance_Frame, text="Employee ID", font=("times new roman", 12, "bold"), bg="white")
        Id_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        EmpId_entry = ttk.Entry(Attendance_Frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 12, "bold"))
        EmpId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name Label
        Name_Label = Label(Attendance_Frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        Name_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Name_entry = ttk.Entry(Attendance_Frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        Name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Dept Label
        Dept_Label = Label(Attendance_Frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        Dept_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        Dept_entry = ttk.Entry(Attendance_Frame, textvariable=self.var_dept, width=20, font=("times new roman", 12, "bold"))
        Dept_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date Label
        Date_Label = Label(Attendance_Frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        Date_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Date_entry = ttk.Entry(Attendance_Frame, textvariable=self.var_date, width=20, font=("times new roman", 12, "bold"))
        Date_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Time Label
        Time_Label = Label(Attendance_Frame, text="Time", font=("times new roman", 12, "bold"), bg="white")
        Time_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Time_entry = ttk.Entry(Attendance_Frame, textvariable=self.var_time, width=20, font=("times new roman", 12, "bold"))
        Time_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Status
        Status_label = Label(Attendance_Frame, text="Attendance Status", font=("times new roman", 12, "bold"), bg="white")
        Status_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Status_combo = ttk.Combobox(Attendance_Frame, textvariable=self.var_attendance, font=("times new roman", 12, "bold"), state="readonly", width=18)
        Status_combo["values"] = ("Status", "Present", "Absent")
        Status_combo.current(0)
        Status_combo.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Button Frame

        Btn_Frame = Frame(Attendance_Frame, bd=2, bg="white", relief=RIDGE)
        Btn_Frame.place(x=0, y=210, width=625, height=38)

        import_btn = Button(Btn_Frame, text="Import CSV", command=self.importCsv, cursor="hand2", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(Btn_Frame, text="Export CSV", command=self.expoertCsv, cursor="hand2", width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(Btn_Frame, text="Update", cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(Btn_Frame, text="Reset", command=self.reset_data, cursor="hand2", width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right Label Frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_Frame.place(x=660, y=5, width=650, height=450)

        # Table Frame
        Table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        Table_Frame.place(x=5, y=5, width=640, height=420)

        # Scroll Bar
        Scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(Table_Frame, column=("Id", "Name", "Department", "Date", "Time", "Status"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.AttendanceReportTable.xview)
        Scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="EmpId")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Status", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("Id", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Status", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ============Fetch Data==========

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # ================Import CSV===============

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"),("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ===============Export CSV===============

    def expoertCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to" + os.path.basename(fln)+ "successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
