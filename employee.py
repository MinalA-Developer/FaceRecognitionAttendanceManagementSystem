from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+0+0")
        self.root.title("Employee Details")
        self.root.resizable(False, False)


        # ===============Variables for employee table===============
        self.var_dept_name = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_type = StringVar()
        self.var_proof_no = StringVar()
        self.var_address = StringVar()

        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        # ===============Variables for department table===============
        self.var_dept_id = StringVar()
        self.var_dep_name = StringVar()




        # First Image
        img = Image.open(r"G:\Python\FaceRecognitionProject\Images\candidaturas-para-estudantes-internacionais-2021-2022-1140x641.jpg")
        img = img.resize((460, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=460, height=130)

        # Second Image
        img1 = Image.open(r"G:\Python\FaceRecognitionProject\Images\slider_image_2.jpg")
        img1 = img1.resize((460, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=460, y=0, width=460, height=130)

        # Third Image
        img2 = Image.open(r"G:\Python\FaceRecognitionProject\Images\temp-1.jpg")
        img2 = img2.resize((460, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=920, y=0, width=460, height=130)

        # Background Image
        img3 = Image.open(r"G:\Python\FaceRecognitionProject\Images\abstract-technology-background-hi-tech-communication-concept-innovation_42421-384.jpg")
        img3 = img3.resize((1350, 690), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1350, height=690)

        title_lbl = Label(bg_img, text="EMPLOYEE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        main_frame = Frame(bg_img, bd= 2, bg="white")
        main_frame.place(x=10, y=50, width=1320, height= 510)

        # Left Label Frame
        Left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"))
        Left_Frame.place(x=10, y=5, width=640, height=490)

        img_left = Image.open(r"G:\Python\FaceRecognitionProject\Images\happy-employees.jpg")
        img_left = img_left.resize((620, 110), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_Frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=625, height=110)

        # Employee Personal Information Frame
        Employee_Personal_Information_Frame = LabelFrame(Left_Frame, bd=2, bg="white", relief=RIDGE, text="Employee Personal Information", font=("times new roman", 12, "bold"))
        Employee_Personal_Information_Frame.place(x=5, y=115, width=625, height=345)

        # Department Name
        Dept_label = Label(Employee_Personal_Information_Frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        Dept_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.Dept_list = []
        self.Dept_combo = ttk.Combobox(Employee_Personal_Information_Frame, textvariable=self.var_dept_name, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.Dept_combo["values"] = self.Dept_list
        self.Dept_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Employee ID
        EmpId_label = Label(Employee_Personal_Information_Frame, text="Employee ID", font=("times new roman", 12, "bold"), bg="white")
        EmpId_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        EmpId_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_id, width=20, font=("times new roman", 12, "bold"))
        EmpId_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Name
        EmpName_label = Label(Employee_Personal_Information_Frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        EmpName_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        EmpName_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_name, width=20, font=("times new roman", 12, "bold"))
        EmpName_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email
        EmpEmail_label = Label(Employee_Personal_Information_Frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        EmpEmail_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        EmpEmail_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_email, width=20, font=("times new roman", 12, "bold"))
        EmpEmail_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(Employee_Personal_Information_Frame, text="Gender", font=("times new roman", 12, "bold"),bg="white")
        Gender_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(Employee_Personal_Information_Frame, textvariable = self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        Gender_combo["values"] = ("Select Gender", "Male", "Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Contact No
        ContactNo_label = Label(Employee_Personal_Information_Frame, text="Contact No", font=("times new roman", 12, "bold"), bg="white")
        ContactNo_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        ContactNo_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_phone, width=20, font=("times new roman", 12, "bold"))
        ContactNo_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Date of Birth
        DOB_label = Label(Employee_Personal_Information_Frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_dob, width=20, font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Date of Join
        DOJ_label = Label(Employee_Personal_Information_Frame, text="DOJ", font=("times new roman", 12, "bold"), bg="white")
        DOJ_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOJ_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_doj, width=20, font=("times new roman", 12, "bold"))
        DOJ_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Proof Type
        Proof_Type_label = Label(Employee_Personal_Information_Frame, text="Proof Type", font=("times new roman", 12, "bold"), bg="white")
        Proof_Type_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Proof_Type_combo = ttk.Combobox(Employee_Personal_Information_Frame, textvariable = self.var_proof_type, font=("times new roman", 12, "bold"), state="readonly", width=18)
        Proof_Type_combo["values"] = ("Select Proof Type", "Aadhaar Card", "Pan Card", "Driving Licence")
        Proof_Type_combo.current(0)
        Proof_Type_combo.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Proof Number
        Proof_No_label = Label(Employee_Personal_Information_Frame, text="Proof Number", font=("times new roman", 12, "bold"), bg="white")
        Proof_No_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Proof_No_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_proof_no, width=20, font=("times new roman", 12, "bold"))
        Proof_No_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label = Label(Employee_Personal_Information_Frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        Address_label.grid(row=5, column=2, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(Employee_Personal_Information_Frame, textvariable = self.var_address, width=20, font=("times new roman", 12, "bold"))
        Address_entry.grid(row=5, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Employee_Personal_Information_Frame, variable = self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=7, column=0)

        radiobtn2 = ttk.Radiobutton(Employee_Personal_Information_Frame, variable = self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=7, column=1)

        # Button Frame
        btn_Frame = Frame(Employee_Personal_Information_Frame, bd=2, bg="white", relief=RIDGE)
        btn_Frame.place(x=0, y=245, width=620, height=40)

        # Save Button
        save_btn = Button(btn_Frame, text="Save", command = self.add_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Update Button
        update_btn = Button(btn_Frame, text="Update", command = self.update_data, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # Delete Button
        delete_btn = Button(btn_Frame, text="Delete", command=self.delete_emp, width=15, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset Button
        reset_btn = Button(btn_Frame, text="Reset", command=self.reset_emp, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Button Frame
        btn_Frame1 = Frame(Employee_Personal_Information_Frame, bd=2, bg="white", relief=RIDGE)
        btn_Frame1.place(x=0, y=280, width=620, height=40)

        # Take a Photo Button
        take_photo_btn = Button(btn_Frame1, text="Take Photo Sample", command=self.generate_dataset, width=30, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        # Update Photo Button
        update_photo_btn = Button(btn_Frame1, text="Update Photo Sample", width=30, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right Label Frame
        Right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE)
        Right_Frame.place(x=660, y=10, width=650, height=490)

        # img_right = Image.open(r"G:\Python\Face RecognitionProject\Images\getty_690855708_348824.jpg")
        # img_right = img_right.resize((630, 120), Image.ANTIALIAS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)
        #
        # f_lbl = Label(Right_Frame, image=self.photoimg_right)
        # f_lbl.place(x=5, y=0, width=635, height=120)


        # ==========Search System==========
        Search_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_Frame.place(x=5, y=0, width=640, height=70)

        # Search Label
        Search_label = Label(Search_Frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Search Combobox
        Search_combo = ttk.Combobox(Search_Frame, textvariable=self.var_search_by, font=("times new roman", 12, "bold"),state="readonly", width=14)
        Search_combo["values"] = ("Select", "Emp_id", "Name", "Phone")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Search Entry
        Search_entry = ttk.Entry(Search_Frame, width=14, textvariable=self.var_search_txt, font=("times new roman", 12, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Search Button
        Search_btn = Button(Search_Frame, text="Search", command=self.search_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3, padx=4)

        # Show all Button
        ShowAll_btn = Button(Search_Frame, text="Show All", command=self.search_data, width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=4)

        # Table Frame
        Table_Frame = Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
        Table_Frame.place(x=5, y=75, width=640, height=210)

        # Scroll Bar
        Scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Table_Frame, column=("dep name", "id", "name", "email", "gender", "contact no", "dob", "doj", "proof type", "proof no", "address", "photo"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.employee_table.xview)
        Scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep name", text="Department")
        self.employee_table.heading("id", text="Employee ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact no", text="Contact No")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("proof type", text="Proof Type")
        self.employee_table.heading("proof no", text="Proof Number")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("photo", text="PhotoSampleStatus")
        self.employee_table["show"] = "headings"

        self.employee_table.column("dep name", width=100)
        self.employee_table.column("id", width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact no", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("proof type", width=100)
        self.employee_table.column("proof no", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("photo", width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


        # Department Frame
        Department_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="Department Details", font=("times new roman", 12, "bold"))
        Department_Frame.place(x=5, y=285, width=640, height=200)

        # Department Search combobox
        Dep_Search_combo = ttk.Combobox(Department_Frame, font=("times new roman", 12, "bold"), state="readonly", width=14)
        Dep_Search_combo["values"] = ("Select", "Dept_ID", "Department")
        Dep_Search_combo.current(0)
        Dep_Search_combo.place(x=5, y=5, width=120, height=25)

        # Department search entry
        Dep_Search_entry = ttk.Entry(Department_Frame, width=14, font=("times new roman", 12, "bold"))
        Dep_Search_entry.place(x=130, y=5, width=120)

        # Department Search Button
        Dep_Search_btn = Button(Department_Frame, text="Search", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        Dep_Search_btn.place(x=255, y=5, width=80, height=25)

        # Show all Button
        Dep_ShowAll_btn = Button(Department_Frame, text="Show All", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        Dep_ShowAll_btn.place(x=340, y=5, width=80, height=25)

        # Department id
        Dep_id_lable = Label(Department_Frame, text="Department ID", font=("times new roman", 12, "bold"), bg="white")
        Dep_id_lable.place(x=5, y=50, width=135, height=20)

        Dep_id_entry = ttk.Entry(Department_Frame, textvariable=self.var_dept_id, width=20, font=("times new roman", 12, "bold"))
        Dep_id_entry.place(x=155, y=50, width=150)

        # Department Name
        Dep_name_label = Label(Department_Frame, text="Department Name", font=("times new roman", 12, "bold"), bg="white")
        Dep_name_label.place(x=15, y=80, width=135, height=20)

        self.Dep_name_entry = ttk.Entry(Department_Frame, textvariable=self.var_dep_name, width=20, font=("times new roman", 12, "bold"))
        self.Dep_name_entry.place(x=155, y=80, width=150)

        # Department Table Frame
        Dep_Table_Frame = Frame(Department_Frame, bd=2, bg="white", relief=RIDGE)
        Dep_Table_Frame.place(x=425, y=0, width=210, height=175)

        # Scroll Bar
        Dep_Scroll_x = ttk.Scrollbar(Dep_Table_Frame, orient=HORIZONTAL)
        Dep_Scroll_y = ttk.Scrollbar(Dep_Table_Frame, orient=VERTICAL)

        self.department_table = ttk.Treeview(Dep_Table_Frame, column=("Dep_id", "Dep_name"), xscrollcommand=Dep_Scroll_x.set, yscrollcommand=Dep_Scroll_y.set)

        Dep_Scroll_x.pack(side=BOTTOM, fill=X)
        Dep_Scroll_y.pack(side=RIGHT, fill=Y)
        Dep_Scroll_x.config(command=self.department_table.xview)
        Dep_Scroll_y.config(command=self.department_table.yview)

        self.department_table.heading("Dep_id", text="Dept ID")
        self.department_table.heading("Dep_name", text="Department")
        self.department_table["show"] = "headings"

        self.department_table.column("Dep_id", width=80)
        self.department_table.column("Dep_name", width=100)

        self.department_table.pack(fill=BOTH, expand=1)
        self.department_table.bind("<ButtonRelease>", self.get_dep)
        self.dep_data()

        # Department Button Frame
        dept_btn_Frame = Frame(Department_Frame, bd=2, bg="white", relief=RIDGE)
        dept_btn_Frame.place(x=5, y=125, width=410, height=35)

        # Department Save Button
        dept_save_btn = Button(dept_btn_Frame, text="Save", command = self.add_department, width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        dept_save_btn.grid(row=0, column=0)

        # Department Update Button
        dept_update_btn = Button(dept_btn_Frame, text="Update", command=self.update_department, width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        dept_update_btn.grid(row=0, column=1)

        # Department Delete Button
        dept_delete_btn = Button(dept_btn_Frame, text="Delete", command=self.delete_department, width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        dept_delete_btn.grid(row=0, column=2)

        # Department Reset Button
        dept_reset_btn = Button(dept_btn_Frame, text="Reset", command=self.reset_department, width=9, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        dept_reset_btn.grid(row=0, column=3)

    # ===============Add values in dept combo and database===============
    def add_department(self):
        activity = self.Dep_name_entry.get().strip()
        try:
            if activity:
                self.Dept_list.append(activity)
                self.Dept_combo["values"] =self.Dept_list
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into department values(%s, %s)", (self.var_dept_id.get(),
                                                                            self.var_dep_name.get()
                                                                            ))
                conn.commit()
                self.dep_data()
                conn.close()
                messagebox.showinfo("Success", "Department Details has been added successfully !!!", parent=self.root)
            else:
                messagebox.showerror("Error", "Please Enter Department Name", parent=self.root)
        except EXCEPTION as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ===============fetch department data===============
    def dep_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from department")
        data = my_cursor.fetchall()

        if len(data) !=0:
            self.department_table.delete(*self.department_table.get_children())
            for i in data:
                self.department_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===============get employee data===============
    def get_dep(self, event=""):
        cursor_focus = self.department_table.focus()
        content = self.department_table.item(cursor_focus)
        data = content["values"]
        self.var_dept_id.set(data[0]),
        self.var_dep_name.set(data[1])

    # ===============Update Department===============
    def update_department(self):
        try:
            Update = messagebox.askyesno("Update", "Do you want to update this department details", parent=self.root)
            if Update>0:
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("update department set dept_name=%s where dept_id=%s",(
                                                                        self.var_dep_name.get(),
                                                                        self.var_dept_id.get()
                                                                    ))
            else:
                if not Update:
                    return
            messagebox.showinfo("Success", "Department details successfully updated !!!", parent=self.root)
            conn.commit()
            self.dep_data()
            conn.close()
        except EXCEPTION as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===============Delete Department===============
    def delete_department(self):
        if self.var_dept_id.get()=="":
            messagebox.showerror("Error", "Department ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Department delete page", "Do you really want to delete this department information", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from department where dept_id=%s"
                    val = (self.var_dept_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Success", "Department details successfully deleted !!!", parent=self.root)
                conn.commit()
                self.dep_data()
                conn.close()
                self.reset_department()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ===============Reset Department===============
    def reset_department(self):
        self.var_dept_id.set("")
        self.var_dep_name.set("")

    # ===============Functions Declaration for add employee===============
    def add_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="MySqlRoot@333",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                               self.var_dept_name.get(),
                                                                                               self.var_id.get(),
                                                                                               self.var_name.get(),
                                                                                               self.var_email.get(),
                                                                                               self.var_gender.get(),
                                                                                               self.var_phone.get(),
                                                                                               self.var_dob.get(),
                                                                                               self.var_doj.get(),
                                                                                               self.var_proof_type.get(),
                                                                                               self.var_proof_no.get(),
                                                                                               self.var_address.get(),
                                                                                               self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee Details has been added successfully !!!", parent=self.root)
                self.reset_emp()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ===============fetch employee data===============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        data = my_cursor.fetchall()

        if len(data) !=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END, values=i)
            conn.commit()
        conn.close()

    # ===============get employee data===============
    def get_cursor(self, event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]

        # self.var_dept_name.set(data[0]),
        # self.var_id.set(data[1]),
        self.var_name.set(data[2]),
        self.var_email.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_phone.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_doj.set(data[7]),
        self.var_proof_type.set(data[8]),
        self.var_proof_no.set(data[9]),
        self.var_address.set(data[10]),
        self.var_radio1.set(data[11])

    # update function
    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this employee details", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set Dep=%s, Name=%s, Email=%s, Gender=%s, Phone=%s, DOB=%s, DOJ=%s, Proof_Type=%s, Proof_No=%s, Address=%s, PhotoSample=%s where Emp_id=%s",(
                                                                                                                                                                            self.var_dept_name.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_doj.get(),
                                                                                                                                                                            self.var_proof_type.get(),
                                                                                                                                                                            self.var_proof_no.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_id.get()
                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee details successfully updated", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)

    # delete function
    def delete_emp(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Employee Delete Page", "Do you want to delete this employee information", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from employee where Emp_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_emp()
                messagebox.showinfo("Success", "Successfully deleted Employee details", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # reset function
    def reset_emp(self):
        self.var_dept_name.set(""),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select Gender"),
        self.var_phone.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_proof_type.set("Select Proof Type"),
        self.var_proof_no.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")

    # ===============Generate data Set or Take photo samples==============
    def generate_dataset(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="Select Gender":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employee")
                my_result = my_cursor.fetchall()
                id=1
                for x in my_result:
                    id+=1
                my_cursor.execute("update employee set Dep=%s, Name=%s, Email=%s, Gender=%s, Phone=%s, DOB=%s, DOJ=%s, Proof_Type=%s, Proof_No=%s, Address=%s, PhotoSample=%s where Emp_id=%s",(
                                                                                                                                                                        self.var_dept_name.get(),
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                        self.var_proof_type.get(),
                                                                                                                                                                        self.var_proof_no.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_id.get()==id+1
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                # self.reset_emp()
                conn.close()

                # =============== Load predefined data on face frontals from opencv ===============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor = 1.3 default value
                    # Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                address = "http://192.168.0.102:8080//video"
                cap.open(address)
                img_id=0
                while True:
                    ret, my_frame = cap.read(0)
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path_name = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path_name, face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed!!!", parent=self.root)

            except EXCEPTION as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ===============search employee data===============

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="MySqlRoot@333", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee where" +self.var_search_by.get() + "LIKE %"+self.var_search_txt.get()+"%")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()














if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
