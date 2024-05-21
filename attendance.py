from tkinter import *
from tkinter import ttk                
from PIL import Image,ImageTk          
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata = []

# creating Student Details Main page

class Attendance:
    def __init__(self, root):                 
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Attendance")

    # ============ Variables ============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        #Image1
        at_img = Image.open(r"Images\23.attendance2.jpg")
        at_img = at_img.resize((1530,220), Image.LANCZOS)
        self.photoat_img = ImageTk.PhotoImage(at_img)
        
        f_lbl = Label(self.root, image=self.photoat_img)
        f_lbl.place(x=1, y=0, width=1530, height=200)

        #Main Frame
        main_frame = Frame(root, bd=2, bg="#c4f1f1")
        main_frame.place(x=15, y=210, width=1500, height=560)

    #Left Label Frame   
        left_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE, text="Student Attendance Details", font=("Coronet", 12, "bold"))
        left_frame.place(x=10, y=10,width=725, height=540)
    #Image2
        lf_img = Image.open(r"Images\22.attendance1.jpg")
        lf_img = lf_img.resize((710,150), Image.LANCZOS)
        self.photolf_img = ImageTk.PhotoImage(lf_img)
        
        f_lbl = Label(left_frame, image=self.photolf_img)
        f_lbl.place(x=3, y=0, width=710, height=150)

    #Student Attendance Information Frame
        left_inside_frame = LabelFrame(left_frame, bd=4, bg="white", relief=RIDGE, font=("Coronet", 12, "bold"))
        left_inside_frame.place(x=10, y=155, width=695, height=355)

#Label Entry
        #Attendence Id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID*:",font=("Coronet", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("Coronet", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        #Roll No
        rollNo_label = Label(left_inside_frame, text="Roll Number*:",font=("Coronet", 13, "bold"), bg="white")
        rollNo_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        atten_roll = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("Coronet", 12, "bold"))
        atten_roll.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        
        #Name
        Name_label = Label(left_inside_frame, text="Name:",font=("Coronet", 13, "bold"), bg="white")
        Name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        aten_name = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("Coronet", 12, "bold"))
        aten_name.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        #Department
        rollNo_label = Label(left_inside_frame, text="Department:",font=("Coronet", 13, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        
        atten_dep = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("Coronet", 12, "bold"))
        atten_dep.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        
        #Time
        time_label = Label(left_inside_frame, text="Time:",font=("Coronet", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        atten_time = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("Coronet", 12, "bold"))
        atten_time.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        #Date
        date_label = Label(left_inside_frame, text="Date:",font=("Coronet", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        
        atten_date = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("Coronet", 12, "bold"))
        atten_date.grid(row=2, column=3, padx=5, pady=5, sticky=W)
        
        #Attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:",font=("Coronet", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        
        self.atten_status = ttk.Combobox(left_inside_frame, font=("Coronet", 12, "bold"), width=18, textvariable=self.var_atten_attendance, state="readonly")
        self.atten_status["values"] = ("Select status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
    #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2, relief=RIDGE, bg="white", padx=8, pady=6)
        btn_frame.place(x=10,y=250, width=668, height=50)
        
        #Import Button
        import_btn = Button(btn_frame, cursor="hand2", command=self.importCSV, text="Import CSV", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=15)
        import_btn.grid(row=0, column=0)
        #Export Button
        export_btn = Button(btn_frame, cursor="hand2", command=self.exportCSV, text="Export CSV", font=("Coronet", 13, "bold"), bg="blue", fg="white", width=15)
        export_btn.grid(row=0, column=1)
        #Update Button
        update_btn = Button(btn_frame, cursor="hand2", text="Update", font=("Coronet", 13, "bold"), bg="blue", fg="white",width=15)
        update_btn.grid(row=0, column=2)
        #Reset Button
        reset_btn = Button(btn_frame, cursor="hand2", text="Reset", command=self.reset_data, font=("Coronet", 13, "bold"), bg="blue", fg="white", width=15)
        reset_btn.grid(row=0, column=3)

    #Right Label Frame   
        right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE, text="Attendance Details", font=("Coronet", 13, "bold"))
        right_frame.place(x=745, y=10,width=740, height=540)

        #Right Inside Frame
        right_inside_frame = LabelFrame(right_frame, bd=4, bg="white", relief=RIDGE, font=("Coronet", 12, "bold"))
        right_inside_frame.place(x=10, y=5, width=710, height=505)

        # ================ Scroll Bar ================
        scroll_x = ttk.Scrollbar(right_inside_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_inside_frame, orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(right_inside_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Display column name
        self.AttendanceReportTable.heading("id", text="Attendence ID")
        self.AttendanceReportTable.heading("roll", text="Roll Number")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendence")
        
        self.AttendanceReportTable["show"] = "headings"

        #set column width
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)



# ======================= Fetch Data =======================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)


    # ======================= Import CSV Data =======================
    def importCSV(self):
        global mydata
        mydata.clear()
        flname = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"), ("All File", "*.*")), parent=self.root)
        with open(flname) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        messagebox.showinfo("Success", "Data imported successfully..")



    # ======================= Export CSV Data =======================
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data found to export.", parent=self.root)
                return False

            flname = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"), ("All File", "*.*")), parent=self.root)
            with open(flname, mode="w", newline="") as myfile:
                export_write =csv.writer(myfile, delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Success", "Data Exported to "+ os.path.basename(flname)+" Successfully..", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent = self.root)


    def get_cursor(self, a=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # incomplete function
    def update_data(self):
        pass

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()