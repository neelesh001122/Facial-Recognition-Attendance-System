from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv


# creating Face Recognition page

class FaceRecognition:
    def __init__(self, root):                 #root is name of home window 
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Face Recognition System")
        self.file_name = f"attendence_report/attendance_{datetime.now().strftime('%Y-%m-%d')}.csv"
        
        #Label Image
        fr_img1 = Image.open(r"Images\5.face_recogn.webp")
        fr_img1 = fr_img1.resize((150,100), Image.LANCZOS)
        self.photofr_img1 = ImageTk.PhotoImage(fr_img1)
        
        f_lbl = Label(self.root, image=self.photofr_img1)
        f_lbl.place(x=0, y=0, width=150, height=100)


        #Label
        title_lbl = Label(self.root, text="Face Recognition System", font=("Coronet", 50, "bold"), bg="#B8BEEE", fg="#0000CC")
        title_lbl.place(x=150, y=0, width=1230, height=100)


        #Label Image
        # tr_img1 = Image.open(r"Images\5.face_recogn.webp")
        # tr_img1 = tr_img1.resize((150,100), Image.LANCZOS)
        # self.phototr_img1 = ImageTk.PhotoImage(tr_img1)
        
        f_lbl = Label(self.root, image=self.photofr_img1)
        f_lbl.place(x=1380, y=0, width=150, height=100)
        
        
        # Top Image1
        top_img1 = Image.open(r"Images\21.Face_reco.png")
        top_img1 = top_img1.resize((1533,680), Image.LANCZOS)
        self.phototop_img1 = ImageTk.PhotoImage(top_img1)
        
        f_lbl = Label(self.root, image=self.phototop_img1)
        f_lbl.place(x=0, y=100, width=1533, height=680)
        
        
        
        
        #Recognition Button
        train_btn = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("Coronet", 18, "bold"), bg="grey", fg="white", width=100)
        train_btn.place(x=375, y=550, width=300, height=40)


# ======================== Attendance ========================
    def mark_attendance(self, std_id, roll, name, depart):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["std_id", "roll", "name", "depart", "time", "date", "status"])

        with open(self.file_name, "r+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])
            
            if ((std_id not in nameList) and (roll not in nameList) and (name not in nameList) and (depart not in nameList)):
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                dtstr = now.strftime("%H:%M:%S")
                f.writelines(f"{std_id},{roll},{name},{depart},{dtstr},{date}, Present \n")




# ======================== Face Recognition Function ========================
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grey_image, scaleFactor, minNeighbour)
            
            coordi = []
            
            for (x, y, w, h) in features:
                
                # cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                id, predict = clf.predict(grey_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                my_cursor = conn.cursor()
                
                # Data to be shown on screen
                my_cursor.execute("select Name from student where Student_id=" + str(id))         # fetch name from database
                name = my_cursor.fetchone()
                if name is not None:
                    # name = name[0]
                    name = "+".join(name)
                else:
                    continue
                
                my_cursor.execute("select Roll from student where Student_id=" + str(id))         # fetch roll no from database
                roll = my_cursor.fetchone()[0]
                roll = f"Roll No: {roll}"
                
                my_cursor.execute("select Dep from student where Student_id=" + str(id))          # fetch department from database
                depart = my_cursor.fetchone()[0]
                depart = f"Department: {depart}"
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))          # fetch Student ID from database
                std_id = my_cursor.fetchone()
                std_id = "+".join(std_id)


                if confidence > 77:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                    cv2.putText(img, f"Student ID:{std_id}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll Number:{roll}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{name}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{depart}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(std_id, roll, name, depart)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
                    cv2.putText(img, "Unknown Face", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                coordi = [x, y, w, y]
                
            return coordi


        def recognize(img, clf, faceCascade):
            coordi = draw_boundry(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()