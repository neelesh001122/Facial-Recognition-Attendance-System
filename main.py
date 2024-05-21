from tkinter import *
from tkinter import messagebox
from tkinter import ttk                # style toolkit
from PIL import Image,ImageTk          # pillow for images
import os
from time import strftime
from datetime import datetime
from studentDetails import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
from help import Help



# creating main page

class Face_Recognition_System:
    def __init__(self, root):                 #root is name of home window 
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Face Recognition System")
        
        #Image1
        img1 = Image.open(r"D:\Python\Projects\Neelesh Project\4.Advance Facial Recognition Attendance System\Images\1.images.jpg")
        img1 = img1.resize((130, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=130, height=130)

        #Image2
        img = Image.open(r"Images\2.Facialbanner.png")
        img = img.resize((1530, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=130, y=0, width=1270, height=130)

        #Image3
        img3 = Image.open(r"Images\1.images.jpg")
        img3 = img3.resize((130, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1400, y=0, width=130, height=130)

        #Background Image
        bg_img = Image.open(r"Images\3.bg_img.webp")
        bg_img = bg_img.resize((1530,660), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        bg_imag = Label(self.root, image=self.photobg_img)
        bg_imag.place(x=0, y=130, width=1530, height=650)

        #Label
        title_lbl = Label(bg_imag, text="Creacted By Neelesh Verma", font=("Coronet", 30, "italic"), bg="#B8BEDD", fg="#006D77")
        title_lbl.place(x=50, y=-2, width=1430, height=50)

            # =============== Time ===============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=("Coronet", 10, "italic"), background='white', foreground='black')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

#Buttons
        #Student Button
        st_bt = Image.open(r"Images\4.studentDetail.jpg")
        st_bt = st_bt.resize((220,220), Image.LANCZOS)
        self.photost_bt = ImageTk.PhotoImage(st_bt)

        b1 = Button(bg_imag, image=self.photost_bt, command=self.student_details, cursor="hand2")
        b1.place(x=215,y=80,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Student Details", command=self.student_details, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=215,y=300,width=220, height=40)


        #Decect Face Button
        fc_bt = Image.open(r"Images\5.face_recogn.webp")
        fc_bt = fc_bt.resize((220,220), Image.LANCZOS)
        self.photofc_bt = ImageTk.PhotoImage(fc_bt)

        b1 = Button(bg_imag, image=self.photofc_bt, cursor="hand2", command=self.face_recognition)
        b1.place(x=515,y=80,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Face Detector", command=self.face_recognition, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=515,y=300,width=220, height=40)


        #Attendence Button
        att_bt = Image.open(r"Images\6.attendence.png")
        att_bt = att_bt.resize((220,220), Image.LANCZOS)
        self.photoatt_bt = ImageTk.PhotoImage(att_bt)

        b1 = Button(bg_imag, image=self.photoatt_bt, cursor="hand2", command=self.attendance_data)
        b1.place(x=815,y=80,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Attendence", command=self.attendance_data, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=815,y=300,width=220, height=40)


        #Help Button
        hp_bt = Image.open(r"Images\7.help.jpg")
        hp_bt = hp_bt.resize((220,220), Image.LANCZOS)
        self.photohp_bt = ImageTk.PhotoImage(hp_bt)

        b1 = Button(bg_imag, image=self.photohp_bt, cursor="hand2", command=self.help_window)
        b1.place(x=1115,y=80,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Help", command=self.help_window, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=1115,y=300,width=220, height=40)


        #Train Button
        tr_bt = Image.open(r"Images\8.trainData.jpg")
        tr_bt = tr_bt.resize((220,220), Image.LANCZOS)
        self.phototr_bt = ImageTk.PhotoImage(tr_bt)

        b1 = Button(bg_imag, image=self.phototr_bt, cursor="hand2", command=self.train_data)
        b1.place(x=215,y=360,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Train Data", cursor="hand2", command=self.train_data, font=("Coronet", 15, "italic"), bg="black", fg="white")
        b1_1.place(x=215,y=580,width=220, height=40)


        #Photos Button
        pt_bt = Image.open(r"Images\9.photos.jpg")
        pt_bt = pt_bt.resize((220,220), Image.LANCZOS)
        self.photopt_bt = ImageTk.PhotoImage(pt_bt)

        b1 = Button(bg_imag, image=self.photopt_bt, cursor="hand2", command=self.open_image)
        b1.place(x=515,y=360,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Photos",cursor="hand2", command=self.open_image, font=("Coronet", 15, "italic"), bg="black", fg="white")
        b1_1.place(x=515,y=580,width=220, height=40)


        #Developer Button
        dv_bt = Image.open(r"Images\10.developer.jpg")
        dv_bt = dv_bt.resize((220,220), Image.LANCZOS)
        self.photodv_bt = ImageTk.PhotoImage(dv_bt)

        b1 = Button(bg_imag, image=self.photodv_bt, cursor="hand2", command=self.developer_window)
        b1.place(x=815,y=360,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Developer", command=self.developer_window, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=815,y=580,width=220, height=40)


        #Exit Button
        ex_bt = Image.open(r"Images\11.exit.jpg")
        ex_bt = ex_bt.resize((220,220), Image.LANCZOS)
        self.photoex_bt = ImageTk.PhotoImage(ex_bt)

        b1 = Button(bg_imag, image=self.photoex_bt, cursor="hand2", command=self.exitfxxn)
        b1.place(x=1115,y=360,width=220, height=220)
        
        b1_1 = Button(bg_imag, text="Exit", command=self.exitfxxn, font=("Coronet", 15, "italic"), bg="black", fg="white", cursor="hand2")
        b1_1.place(x=1115,y=580,width=220, height=40)


# ===================== select photos from directory for Training =====================
    def open_image(self):
        os.startfile("data")


    # ===================== Exit Function =====================
    def exitfxxn(self):
        self.exitfxxn = messagebox.askyesno("Face Recognition", "Are you sure?", parent=self.root)
        if self.exitfxxn > 0:
            self.root.destroy()
        else:
            return

# ===================== Function Buttons =====================
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
