from tkinter import *
from tkinter import ttk                # style toolkit
from PIL import Image,ImageTk          # pillow for images
from tkinter import messagebox
import mysql.connector
import cv2


# creating Student Details Main page

class Student:
    def __init__(self, root):                 #root is name of home window 
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Student Details")


    #=================== Define Variables ===================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        #Background Image
        bg_st_img = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\14.bg_st.jpg")
        bg_st_img = bg_st_img.resize((1530,780), Image.LANCZOS)
        self.photobg_st_img = ImageTk.PhotoImage(bg_st_img)
        
        bg_imag = Label(self.root, image=self.photobg_st_img)
        bg_imag.place(x=0, y=0, width=1530, height=780)


        #Image1
        st_img1 = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\4.studentDetail.jpg")
        st_img1 = st_img1.resize((151,100), Image.LANCZOS)
        self.photost_img1 = ImageTk.PhotoImage(st_img1)
        
        f_lbl = Label(self.root, image=self.photost_img1)
        f_lbl.place(x=1, y=0, width=151, height=100)


        #Label
        title_lbl = Label(bg_imag, text="Student Management System", font=("Coronet", 50, "bold"), bg="#B8BEDD", fg="#006D77")
        title_lbl.place(x=150, y=-2, width=1230, height=100)


        #Image2
        st_img2 = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\4.studentDetail.jpg")
        st_img2 = st_img2.resize((151,100), Image.LANCZOS)
        self.photost_img2 = ImageTk.PhotoImage(st_img2)
        
        f_lbl = Label(self.root, image=self.photost_img2)
        f_lbl.place(x=1380, y=0, width=151, height=100)


        #Main Frame
        main_frame = Frame(bg_imag, bd=2, bg="#c4f1f1")
        main_frame.place(x=15, y=110, width=1500, height=655)

    #Left Label Frame   
        left_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE, text="Student Details", font=("Coronet", 12, "bold"))
        left_frame.place(x=10, y=10,width=730, height=630)
        
        #Image
        img_left = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\15.st_dt_img.jpg")
        img_left = img_left.resize((710,130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=130)
        
        #Current Course Information
        current_course_frame = LabelFrame(left_frame, bd=4, bg="white", relief=RIDGE, text="Current Course Information", font=("Coronet", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=710, height=120)
        
        #Department
        dep_label = Label(current_course_frame, text="Department*",font=("Coronet", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("Coronet", 12, "bold"), width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Information Technnology", "Civil", "Mechanical", "Chemical", "Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx= 5, pady=10, sticky=W)
        
        #Course Year
        course_label = Label(current_course_frame, text="Course Year",font=("Coronet", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("Coronet", 12, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "FE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx= 5, pady=10, sticky=W)
        
        #Year
        year_label = Label(current_course_frame, text="Year",font=("Coronet", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("Coronet", 12, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2020-24", "2021-25", "2022-26", "2023-27", "2024-28")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx= 5, pady=10, sticky=W)
        
        #Semester
        sem_label = Label(current_course_frame, text="Semester",font=("Coronet", 13, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        
        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("Coronet", 12, "bold"), width=20, state="readonly")
        sem_combo["values"] = ("Select Semester", "Sem-1", "Sem-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx= 5, pady=10, sticky=W)
        
        
        #Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=4, bg="white", relief=RIDGE, text="Class Student Information", font=("Coronet", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=710, height=340)
        
        #Student Id
        studentId_label = Label(class_student_frame, text="StudentID*:",font=("Coronet", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=("Coronet", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #Student Name
        studentName_label = Label(class_student_frame, text="Student Name*:",font=("Coronet", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("Coronet", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #Class Division
        classDiv_label = Label(class_student_frame, text="Class Division:",font=("Coronet", 13, "bold"), bg="white")
        classDiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        div_entry = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("Coronet", 12, "bold"), width=18, state="readonly")
        div_entry["values"] = ("Select Division", "A", "B", "C")
        div_entry.current(0)
        div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #Roll Number
        rollNo_label = Label(class_student_frame, text="Roll Number:",font=("Coronet", 13, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        rollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("Coronet", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        #Gender
        gender_label = Label(class_student_frame, text="Gender:",font=("Coronet", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_entry = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("Coronet", 12, "bold"), width=18, state="readonly")
        gender_entry["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_entry.current(0)
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        #Student DOB
        student_dob_label = Label(class_student_frame, text="DOB:",font=("Coronet", 13, "bold"), bg="white")
        student_dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        student_dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("Coronet", 12, "bold"))
        student_dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        #Student Email
        email_label = Label(class_student_frame, text="Email:",font=("Coronet", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("Coronet", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        #Student Phone Number
        phone_no_label = Label(class_student_frame, text="Phone Number:",font=("Coronet", 13, "bold"), bg="white")
        phone_no_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("Coronet", 12, "bold"))
        phone_no_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        #Student Address
        DDRESS_label = Label(class_student_frame, text="Address:",font=("Coronet", 13, "bold"), bg="white")
        DDRESS_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        DDRESS_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("Coronet", 12, "bold"))
        DDRESS_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        #Teacher Name
        teacher_name_label = Label(class_student_frame, text="Teacher Name:",font=("Coronet", 13, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("Coronet", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        #Radio Buttons
        self.var_radio = StringVar()
        radioBttton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, cursor="hand2", text="Take Photo Sample", value="Yes")
        radioBttton1.grid(row=6, column=0)
        
        radioBttton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, cursor="hand2", text="No Photo Sample", value="No")
        radioBttton2.grid(row=6, column=1)
        
        #Button Frame
        btn_frame = Frame(class_student_frame,bd=2, relief=RIDGE, bg="white", padx=8, pady=6)
        btn_frame.place(x=0,y=210, width=700, height=50)
        
        #Save Button
        save_btn = Button(btn_frame, command=self.add_data, cursor="hand2", text="Save", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=16)
        save_btn.grid(row=0, column=0)
        #Update Button
        update_btn = Button(btn_frame, command=self.update_data, cursor="hand2", text="Update", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=16)
        update_btn.grid(row=0, column=1)
        #Delete Button
        delete_btn = Button(btn_frame, command=self.delete_data, cursor="hand2", text="Delete", font=("Coronet", 13, "bold"), bg="blue", fg="white",width=16)
        delete_btn.grid(row=0, column=2)
        #Reset Button
        reset_btn = Button(btn_frame, command=self.reset_data, cursor="hand2", text="Reset", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=16)
        reset_btn.grid(row=0, column=3)
        
        #Button Frame
        btn_frame1 = Frame(class_student_frame,bd=2, relief=RIDGE, bg="white", padx=8, pady=2)
        btn_frame1.place(x=0,y=270, width=700, height=40)
        
        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, cursor="hand2", text="Take Photo Sample", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=33)
        take_photo_btn.grid(row=0, column=1)
        
        update_photo_btn = Button(btn_frame1, cursor="hand2", text="Update Photo Sample", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=33)
        update_photo_btn.grid(row=0, column=2)




    #Right Label Frame   
        right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE, text="Student Details", font=("Coronet", 13, "bold"))
        right_frame.place(x=750, y=10,width=730, height=630)
        
        #Image
        img_right = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\16.st_dt_img.jpg")
        img_right = img_right.resize((710,130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)


        #========== Search System ==========
        #Current Course Informationṇṇ
        search_frame = LabelFrame(right_frame, bd=4, bg="white", relief=RIDGE, text="Search System", font=("Coronet", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)
        
        search_label = Label(search_frame, text="Search By:",font=("Coronet", 15, "bold"), bg="white", fg="grey")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Coronet", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Name", "Roll Number", "Phone Number", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx= 5, pady=10, sticky=W)
        
        search_entry = ttk.Entry(search_frame, width=18, font=("Coronet", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn = Button(search_frame, text="Search", font=("Coronet", 12, "bold"), bg="blue", fg="white", width=9)
        search_btn.grid(row=0, column=3, padx=2)
        
        showAll_btn = Button(search_frame, text="Show All", font=("Coronet", 12, "bold"), bg="blue", fg="white", width=9)
        showAll_btn.grid(row=0, column=4, padx=2)
        
        
        #Table Frame
        table_frame = Frame(right_frame, bd=4, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=390)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        
        self.student_table.pack(fill=BOTH, expand=1)
        
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()    # to show data in rifht frame table





# ===================== Function Buttons =====================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Fill * Manditory Details, All Fields are required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_dep.get(),
                                                                self.var_course.get(),
                                                                self.var_year.get(),
                                                                self.var_sem.get(),
                                                                self.var_std_id.get(),
                                                                self.var_std_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_email.get(),
                                                                self.var_phone.get(),
                                                                self.var_address.get(),
                                                                self.var_teacher.get(),
                                                                self.var_radio.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)



    # ================= Fetch Data =================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            
            conn.commit()
        conn.close()


    # =========================== Get Courser (To select data from table and update it) ===========================
    def get_cursor(self, event=""):
        cursor_focous = self.student_table.focus()
        content = self.student_table.item(cursor_focous)
        data = content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])


    # ====================== Update Function ======================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Fill * Manditory Details, All Fields are required.", parent=self.root)

        else:
            try:
                Upadate = messagebox.askyesno("Update", "Do you want to update this details?", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_sem.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_radio.get(),
                                                            self.var_std_id.get()
                                                        ))
                else:
                    if not Upadate:
                        return 
                messagebox.showinfo("Success", "Details updated successfully.", parent=self.root)

                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)



    # ====================== Delete Function ======================
    def delete_data(self):
        if self.var_std_id == "":
            messagebox.showerror("Error", "Student ID must be required.", parent=self.root)
        
        else:
            try:
                delete = messagebox.askyesno("Delete Attention", "Do you want to delete this data?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Delete", "Student data deleted successfully.", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


    #  ====================== Reset Function ======================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set("")





# ====================== Generate data set or take sameple ======================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Fill * Manditory Details, All Fields are required.", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_sem.get(),
                                                            self.var_std_name.get(),
                                                            self.var_div.get(),
                                                            self.var_roll.get(),
                                                            self.var_gender.get(),
                                                            self.var_dob.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_address.get(),
                                                            self.var_teacher.get(),
                                                            self.var_radio.get(),
                                                            self.var_std_id.get()==id+1
                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ================================= Load predefined data on face frontal from open cv =================================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   #file used for object detection
                
                def face_cropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # convert color image to grey
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
                    # scaling factor = 1.3
                    # minimun neighbour = 5
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                capture = cv2.VideoCapture(0)     # opening camera
                img_id = 0
                while True:
                    ret, my_frame = capture.read()           #read captured image
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
                        cv2.imshow("Cropped Face", face)
                    
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                capture.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result", "Generating dataset completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()