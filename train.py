from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

# creating Training page

class Train:
    def __init__(self, root):                 #root is name of home window 
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Train Data")
        
        #Label Image
        tr_img1 = Image.open(r"Images\17.train1.jpg")
        tr_img1 = tr_img1.resize((150,100), Image.LANCZOS)
        self.phototr_img1 = ImageTk.PhotoImage(tr_img1)
        
        f_lbl = Label(self.root, image=self.phototr_img1)
        f_lbl.place(x=0, y=0, width=150, height=100)


        #Label
        title_lbl = Label(self.root, text="Train Data", font=("Coronet", 50, "bold"), bg="#B8BEEE", fg="#0000CC")
        title_lbl.place(x=150, y=0, width=1230, height=100)


        #Label Image
        # tr_img2 = Image.open(r"Images\17.train1.jpg")
        # tr_img2 = tr_img2.resize((151,100), Image.LANCZOS)
        # self.phototr_img2 = ImageTk.PhotoImage(tr_img2)
        
        f_lbl = Label(self.root, image=self.phototr_img1)
        f_lbl.place(x=1380, y=0, width=150, height=100)
        
        
        # Top Image1
        top_img1 = Image.open(r"Images\18.train2.jpg")
        top_img1 = top_img1.resize((450,250), Image.LANCZOS)
        self.phototop_img1 = ImageTk.PhotoImage(top_img1)
        
        f_lbl = Label(self.root, image=self.phototop_img1)
        f_lbl.place(x=0, y=100, width=450, height=250)
        
        # Top Image2
        top_img2 = Image.open(r"Images\19.train3.jpg")
        top_img2 = top_img2.resize((630,250), Image.LANCZOS)
        self.phototop_img2 = ImageTk.PhotoImage(top_img2)
        
        f_lbl = Label(self.root, image=self.phototop_img2)
        f_lbl.place(x=450, y=100, width=630, height=250)
        
        # Top Image3
        # tr_img1 = Image.open(r"Images\17.train1.jpg")
        # tr_img1 = tr_img1.resize((151,100), Image.LANCZOS)
        # self.phototr_img1 = ImageTk.PhotoImage(tr_img1)
        
        f_lbl = Label(self.root, image=self.phototop_img1)
        f_lbl.place(x=1080, y=100, width=450, height=250)
        
        
        #Train Button
        train_btn = Button(self.root, text="Train Data", cursor="hand2", command=self.train_classifier, font=("Coronet", 45, "bold"), bg="black", fg="white", width=100)
        train_btn.place(x=0, y=350, width=1530, height=100)
        
        
        #Bottom Image
        bot_img = Image.open(r"Images\20.train4.jpg")
        bot_img = bot_img.resize((1530,330), Image.LANCZOS)
        self.photobot_img = ImageTk.PhotoImage(bot_img)
        
        f_lbl = Label(self.root, image=self.photobot_img)
        f_lbl.place(x=0, y=450, width=1530, height=330)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")       #L for gray scale image conversion
            imageNp = np.array(img, "uint8")         # to convert image in grids steps starts from here
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)
        
        # =================== Train the classifier and save ===================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets Completed!")
        







if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()