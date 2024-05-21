from tkinter import *              
from PIL import Image,ImageTk         


# creating Student Details Main page

class Help:
    def __init__(self, root):                  
        self.root = root
        self.root.geometry("1530x780+-6+0")
        self.root.title("Help")
        
        #Label Image
        help_img = Image.open(r"Images\7.help.jpg")
        help_img = help_img.resize((150,100), Image.LANCZOS)
        self.photohelp_img = ImageTk.PhotoImage(help_img)
        
        f_lbl = Label(self.root, image=self.photohelp_img)
        f_lbl.place(x=0, y=0, width=150, height=100)


        #Label
        title_lbl = Label(self.root, text="Help", font=("Coronet", 50, "bold"), bg="#B8BEEE", fg="#0000CC")
        title_lbl.place(x=150, y=0, width=1230, height=100)


        #Label Image
        
        f_lbl = Label(self.root, image=self.photohelp_img)
        f_lbl.place(x=1380, y=0, width=150, height=100)
        
        
        #Background Image
        bg_img = Image.open(r"Images\26.help.jpg")
        bg_img = bg_img.resize((1530,680), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img)
        
        f_lbl = Label(self.root, image=self.photobg_img)
        f_lbl.place(x=0, y=100, width=1530, height=680)


        label = Label(f_lbl, text="Email: neelesh001122@gmail.com",font=("Coronet", 13, "bold"), bg="white")
        label.place(x=620, y=250)





if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()