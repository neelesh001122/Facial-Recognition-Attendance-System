from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()



class LoginPage:
    def __init__(self, root):
        self.root =root
        self.root.title("Login Page")
    # Setting Main page size
        self.root.geometry("1530x780+-6+0")
    
    #  Set Backgrounṇd Image
        bg_image = Image.open("Images/bg.jpg")
        bg_image = bg_image.resize((1530, 780), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1530, height=780)

    # Frame for login
        frame = Frame(self.root, bg="black")
        frame.place(x=590, y=165, width=350, height=450)

    # Login Image
        log_img = Image.open("Images/login.jpg")
        log_img = log_img.resize((100,100), Image.LANCZOS)
        self.log = ImageTk.PhotoImage(log_img)
        
        lbl_log = Label(image=self.log, bg="black", borderwidth=0)
        lbl_log.place(x=715, y=165, width=100, height=100)

    #  Labe of Login
        login = Label(frame, text="Login", font=("Helvetica", 20, "italic"),bg="black", fg="white")
        login.place(x=137, y=100)

# Username
    # Username Icon
        user_icon = Image.open("Images/user.jpg")
        user_icon = user_icon.resize((25,25), Image.LANCZOS)
        self.userico = ImageTk.PhotoImage(user_icon)
        lbl_bg = Label(frame, image=self.userico)
        lbl_bg.place(x=35, y=150, width=25, height=25)

    # Label for username
        username_lbl = Label(frame, text="Username", font=("Helvetica", 15, "italic"),bg="black", fg="white")
        username_lbl.place(x=60, y=150)
    # Entry fill for username
        self.userEntry = ttk.Entry(frame, font=("Helvetica", 15, "bold"))
        self.userEntry.place(x=30, y=185, width=290)

# Password
    # Username Icon
        pass_icon = Image.open("Images/pass.jpg")
        pass_icon = pass_icon.resize((25,25), Image.LANCZOS)
        self.passico = ImageTk.PhotoImage(pass_icon)
        lbl_bg = Label(frame, image=self.passico)
        lbl_bg.place(x=35, y=225, width=25, height=25)
    # Label for password
        password_lbl = Label(frame, text="Password", font=("Helvetica", 15, "italic"),bg="black", fg="white")
        password_lbl.place(x=60, y=225)
    # Entry fill for password
        self.passEntry = ttk.Entry(frame, font=("Helvetica", 15, "bold"))
        self.passEntry.place(x=30, y=260, width=290)
        self.passEntry.config(show="*")

    # Login Button
        login_btn = Button(frame, text="Login", command=self.login_fxn, font=("Helvetica", 15, "italic"), bd=2, relief=RIDGE, fg="white", bg="green", activeforeground="white", activebackground="blue")    # actice foreground and backgroung is used to assign color on click
        login_btn.place(x=115, y=310, width=120, height=35)

    # Register Button
        register_btn = Button(frame, command=self.register_win, text="New User Register", font=("Helvetica", 10, "italic"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")    # actice foreground and backgroung is used to assign color on click
        register_btn.place(x=12, y=368, width=160)

    # Forgot Password Button
        forgot_btn = Button(frame, command=self.froget_password_window, text="Forget Password", font=("Helvetica", 10, "italic"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")    # actice foreground and backgroung is used to assign color on click
        forgot_btn.place(x=6, y=390, width=160)


# ================== Functions ==================

    def register_win(self):
        self.new_win = Toplevel(self.root)
        self.app = RegisterPage(self.new_win)


    def login_fxn(self):
        if self.userEntry.get() == "" or self.passEntry.get() == "":
            messagebox.showerror("Error","Please enter username and password.")
        
        elif self.userEntry.get() == "neelesh" and self.passEntry.get() == "1234":
            messagebox.showinfo("Success","Welcome to My login page.")
        
        else:
            try:             
                conn = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "",
                                            database = "login_system"
                                        )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where username=%s and password=%s", (
                                                                                            self.userEntry.get(),
                                                                                            self.passEntry.get()
                                                                                        ))
                row = my_cursor.fetchone()
                # Print Row
                if row == None:
                    messagebox.showerror("Error", "Invalid username and password")
                else:
                    open_main = messagebox.askyesno("Confirm", "Access only admin")
                    if open_main > 0:
                        self.new_win = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_win)    # Enter the name of class and open in new_win to open your main project
                        # messagebox.showinfo("Success", "Login Successful", parent=self.root)  
                    
                    else:
                        if not open_main:
                            return
                
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")

    # ============================= Forget password Function and window =============================
    def froget_password_window(self):
        if self.userEntry.get() == "":
            messagebox.showerror("Error","Please Enter username to forget password.")
        else:
            try:             
                conn = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "",
                                            database = "login_system"
                                        )
                my_cursor = conn.cursor()
                query = ("select * from register where username=%s")
                value = (self.userEntry.get(),)
                my_cursor.execute(query, value)
                row =  my_cursor.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error","Please enter valid username")
                else:
                    conn.close()
                    # Creating forget pass window
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("380x450+580+170")
                    lbl_forgetPass = Label(self.root2, text="Forget Password",font=("Helvetica", 20, "italic"), fg="green")
                    lbl_forgetPass.place(x=5, y=10,relwidth=1)
                # Label for Security Ques
                    security_ques_resetlbl = Label(self.root2, text="Select Security Question", font=("Helvetica", 15, "italic"), fg="black")
                    security_ques_resetlbl.place(x=65, y=80)
                # Entry fill for Security Ques
                    self.securityResetEntry = ttk.Combobox(self.root2, font=("Helvetica", 14, "bold"), state="readonly")
                    self.securityResetEntry['values'] = ("Select", "Your Birth Place", "Your Father's Name", "Your Mother's Name", "Your Pet Name", "Your Bestfriend Name")
                    self.securityResetEntry.current(0)
                    self.securityResetEntry.place(x=65, y=110, width=250)

                # Label for Security Answer
                    security_ans_reset_lbl = Label(self.root2, text="Security Answer", font=("Helvetica", 15, "italic"),fg="black")
                    security_ans_reset_lbl.place(x=65, y=150)
                # Entry fill for Security Answer
                    self.security_ans_resetEntry = ttk.Entry(self.root2, font=("Helvetica", 15, "bold"))
                    self.security_ans_resetEntry.place(x=65, y=180, width=250)

                # Label for New Password
                    new_pass_resetlbl = Label(self.root2, text="New Password", font=("Helvetica", 15, "italic"),fg="black")
                    new_pass_resetlbl.place(x=65, y=220)
                # Entry fill for New Password
                    self.new_pass_resetEntry = ttk.Entry(self.root2, font=("Helvetica", 15, "bold"))
                    self.new_pass_resetEntry.place(x=65, y=250, width=250)
            
                # Button for reset
                    reset_btn = Button(self.root2, command=self.reset_pass, text="Reset", font=("Helvetica", 15, "italic"),fg="white", bg="black")
                    reset_btn.place(x=140, y=300, width=100)
            
                    # Forget window creation end
            
            
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")


    # ============================= Reset Btn Function =============================
    def reset_pass(self):
        if self.securityResetEntry.get() == "Select":
            messagebox.showerror("Error", "Please select security question.", parent=self.root2)
        elif self.security_ans_resetEntry.get() == "":
            messagebox.showerror("Error", "Please enter security answer.", parent=self.root2)
        elif self.new_pass_resetEntry.get() == "":
            messagebox.showerror("Error", "Please enter new password.", parent=self.root2)
        else:
            try:  
                conn = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "",
                                            database = "login_system"
                                        )
                my_cursor = conn.cursor()
                query = ("select * from register where username=%s and securityQues=%s and securityAns=%s")
                value = (self.userEntry.get(), self.securityResetEntry.get(), self.security_ans_resetEntry.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter correct answer.", parent=self.root2)
                else:
                    query = ("update register set password=%s where username=%s")
                    value = (self.new_pass_resetEntry.get(),self.userEntry.get())
                    my_cursor.execute(query, value)
                    
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Password reset successfully. Now login using new password.", parent=self.root)
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")


class RegisterPage:
    def __init__(self, root):
        self.root =root
        self.root.title("Register Page")
    # Setting Main page size
        self.root.geometry("1530x780+-6+0")
    
# ======================= Defining Variables =======================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_username = StringVar()
        self.var_securityQues = StringVar()
        self.var_securityAns = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
    
    #  Set Background Image
        bg_image = Image.open("Images/bg_reg.jpg")
        bg_image = bg_image.resize((1530, 780), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1530, height=780)

    # Frame for login
        frame = Frame(self.root, bg="white")
        frame.place(x=340, y=115, width=850, height=550)

    #  Labe of Register Here
        login = Label(frame, text="Create New Account", font=("Helvetica", 20, "italic"), fg="black", bg='white')
        login.place(x=20, y=20)


    # Label for First name
        fname_lbl = Label(frame, text="First Name", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        fname_lbl.place(x=80, y=100)
    # Entry fill for First name
        self.fEntry = ttk.Entry(frame, textvariable=self.var_fname, font=("Helvetica", 14, "bold"))
        self.fEntry.place(x=80, y=135, width=250)

    # Label for Last name
        lname_lbl = Label(frame, text="Last Name", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        lname_lbl.place(x=450, y=100)
    # Entry fill for Last name
        self.lEntry = ttk.Entry(frame, textvariable=self.var_lname, font=("Helvetica", 15, "bold"))
        self.lEntry.place(x=450, y=135, width=250)

    # Label for Contact No
        contact_lbl = Label(frame, text="Contact Number", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        contact_lbl.place(x=80, y=180)
    # Entry fill for Contact No
        self.contactEntry = ttk.Entry(frame, textvariable=self.var_contact, font=("Helvetica", 15, "bold"))
        self.contactEntry.place(x=80, y=215, width=250)

    # Label for Username
        username_lbl = Label(frame, text="Username", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        username_lbl.place(x=450, y=180)
    # Entry fill for username
        self.usernameEntry = ttk.Entry(frame, textvariable=self.var_username, font=("Helvetica", 15, "bold"))
        self.usernameEntry.place(x=450, y=215, width=250)

    # Label for Security Ques
        security_ques_lbl = Label(frame, text="Select Security Question", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        security_ques_lbl.place(x=80, y=260)
    # Entry fill for Security Ques
        self.securityEntry = ttk.Combobox(frame, textvariable=self.var_securityQues, font=("Helvetica", 14, "bold"), state="readonly")
        self.securityEntry['values'] = ("Select", "Your Birth Place", "Your Father's Name", "Your Mother's Name", "Your Pet Name", "Your Bestfriend Name")
        self.securityEntry.current(0)
        self.securityEntry.place(x=80, y=295, width=250)

    # Label for Security Answer
        security_ans_lbl = Label(frame, text="Security Answer", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        security_ans_lbl.place(x=450, y=260)
    # Entry fill for Security Answer
        self.security_ansEntry = ttk.Entry(frame, textvariable=self.var_securityAns, font=("Helvetica", 15, "bold"))
        self.security_ansEntry.place(x=450, y=295, width=250)

    # Label for Password
        password_lbl = Label(frame, text="Password", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        password_lbl.place(x=80, y=340)
    # Entry fill for Password
        self.passwordEntry = ttk.Entry(frame, textvariable=self.var_pass, font=("Helvetica", 15, "bold"))
        self.passwordEntry.place(x=80, y=375, width=250)

    # Label for Confirm Password
        conf_password_lbl = Label(frame, text="Confirm Password", font=("Helvetica", 15, "italic"),bg="white", fg="black")
        conf_password_lbl.place(x=450, y=340)
    # Entry fill for Confirm Password
        self.conf_passwordEntry = ttk.Entry(frame, textvariable=self.var_confpass, font=("Helvetica", 15, "bold"))
        self.conf_passwordEntry.place(x=450, y=375, width=250)

    # Check Box
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree the terms and conditions.", font=("Helvetica", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=80, y=420)

    # Register Now Button
        regnowbtn = Button(frame, command=self.register_data, text="Register Now", font=("Helvetica", 15, "bold"), bg="green", fg="white", activebackground="green", activeforeground="black", width=15)
        regnowbtn.place(x=80, y=460)

    # Login Button
        loginbtn = Button(frame, command=self.return_login_window, text="Login", font=("Helvetica", 15, "bold"), bg="green", fg="white", activebackground="green", activeforeground="black", width=15)
        loginbtn.place(x=450, y=460)


# ======================= Functions =======================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_username.get() == "" or self.var_securityQues.get() == "Select" or self.var_securityAns.get() == "" or self.var_pass.get() == "" or self.var_confpass.get() == "":
            messagebox.showerror("Error", "All fields are required.")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same.")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please accept terms and condition.")
        else:
            try:
                conn = mysql.connector.connect(
                                            host = "localhost",
                                            user = "root",
                                            password = "",
                                            database = "login_system"
                                        )
                my_cursor = conn.cursor()
                query = ("select * from register where username = %s")
                value = (self.var_username.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Username already exists.")
                else:
                    my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                                    self.var_fname.get(),
                                                                                                    self.var_lname.get(),
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_username.get(),
                                                                                                    self.var_securityQues.get(),
                                                                                                    self.var_securityAns.get(),
                                                                                                    self.var_pass.get()
                                                                                                ))
                    messagebox.showinfo("Success", "Register Suuccessfully.")
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}")


    def return_login_window(self):
        self.root.destroy()





if __name__ == "__main__":
    main()