from tkinter import *
from tkinter import ttk               
from PIL import Image,ImageTk         
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

# creating Student Details Main page

class Developer:
    def __init__(self, root):                  
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Developer")
        
        #Label Image
        dev_img = Image.open(r"Images\10.developer.jpg")
        dev_img = dev_img.resize((150,100), Image.LANCZOS)
        self.photodev_img = ImageTk.PhotoImage(dev_img)
        
        f_lbl = Label(self.root, image=self.photodev_img)
        f_lbl.place(x=0, y=0, width=150, height=100)


        #Label
        title_lbl = Label(self.root, text="Developer", font=("Coronet", 50, "bold"), bg="#B8BEEE", fg="#0000CC")
        title_lbl.place(x=150, y=0, width=1230, height=100)


        #Label Image
        
        f_lbl = Label(self.root, image=self.photodev_img)
        f_lbl.place(x=1380, y=0, width=150, height=100)
        
        
        #Background Image
        bg_img = Image.open(r"Images\25.Developer1.jpg")
        bg_img = bg_img.resize((1530,680), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        f_lbl = Label(self.root, image=self.photobg_img)
        f_lbl.place(x=0, y=100, width=1530, height=680)

        # Frame
        frame1 = Frame(f_lbl, bd=2,bg="#988C89")
        frame1.place(x=1000, y=0, width=500, height=600)

        #Frame Image
        fr_img = Image.open(r"Images\nee.jpg")
        fr_img = fr_img.resize((200,250), Image.LANCZOS)
        self.photofr_img = ImageTk.PhotoImage(fr_img)
        
        f_lbl = Label(frame1, image=self.photofr_img)
        f_lbl.place(x=300, y=0, width=200, height=250)
        
        # Developer Info
        label = Label(frame1, text="Project Created By:",font=("Coronet", 14, "bold"), bg="#988C89")
        label.grid(row=0,column=0)
        
        label2 = Label(frame1, text="Neelesh Verma",font=("Coronet", 20, "bold"), bg="#988C89")
        label2.grid(row=1,column=0)

        label2 = Label(frame1, text="\n\n Description: \n \nA face recognition attendance system \nautomatically identifies and confirms a \nperson's identity and records \nattendance based on their face \ndetection. ",font=("Coronet", 12), bg="#988C89", )
        label2.grid(row=4,column=0)
        
        label3 = Label(frame1, text="\n\n\n\nLIBRARIES USED: ",font=("Coronet", 12), bg="#988C89", )
        label3.grid(row=5,column=0)
        
        label3 = Label(frame1, text="\n- Tkinter \n - PIL \n - OS \n - DateTime \n - OpenCV \n - Numpy \n - MySQL Connector",font=("Coronet", 12), bg="#988C89", )
        label3.grid(row=6,column=0)
        
        btn = Button(frame1, cursor="hand2", text="Github",command=self.web_browser, font=("Coronet", 13, "bold"), bg="blue", fg="white",width=15)
        btn.grid(row=6, column=1)

    def web_browser(self):
        webbrowser.open("https://github.com/neelesh001122", new=1)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()