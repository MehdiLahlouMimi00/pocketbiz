from tkinter import *
import sqlite3
import os
from tkinter import messagebox
from DashBoard import dashboard
import email

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("PocketBiz")
        self.root.geometry("500x600")
        
        self.Set_Position()
        self.Login_Frame()
        self.Credentials()
        

    def Set_Position(self):
        x = (self.root.winfo_screenwidth() / 2) - (500 / 2)
        y = (self.root.winfo_screenheight() / 2) - (600 / 2)
        self.root.geometry(f"+{int(x)}+{int(y)}")

    def Login_Frame(self):
        self.login_frame = Frame(self.root)
        self.login_frame.place(width=500, height=600)

    def Credentials(self):
        self.username=StringVar() 
        self.password=StringVar()
        
        title = Label(self.login_frame, text="Login System", font=("montserrat", 30, "bold"))
        title.place(x=0, y=20, relwidth=1)

        username = Label(self.login_frame, text="Username", font=("Andalus", 15), fg="black")
        username.place(x=70, y=130)
        textbox_username = Entry(self.login_frame,textvariable=self.username, font=("Times new roman", 20), bg="#d3d3d3")
        textbox_username.place(x=70, y=150, width=350)

        password = Label(self.login_frame, text="Password", font=("Andalus", 15), fg="black")
        password.place(x=70, y=260)
        textbox_password = Entry(self.login_frame,textvariable=self.password,show="*", font=("Times new roman", 20), bg="#d3d3d3")
        textbox_password.place(x=70, y=280, width=350)

        login_button = Button(self.login_frame,command=self.Login,  text="Log in", font=("montserrat", 20), bg="#00B0F0")
        login_button.place(x=70, y=370, width=350,height=60)
        
        line=Label(self.login_frame, bg="black") 
        line.place(x=70, y=457, width=350, height=2)
        line_text=Label(self.login_frame,text="OR",font=("montserrat", 15))
        line_text.place(x=230, y=445)
        
        forgot_password=Button(self.login_frame,text="Forgot Password",command=self.Forgot_Password, font=("montserrat,20"), fg= "black")
        forgot_password.place(x= 180, y=470)
        
    
    def Login(self): 
        con = sqlite3.connect(database=r'employee.db')
        cur=con.cursor()
        try : 
            if self.username.get ()=="" or self.password.get()=="":
                messagebox. showerror ("Error", f"Please enter all the data" ,parent=self.root)
            else:
                cur.execute("select role from employee where id=? and password=?",(self.username.get(),self.password.get()))
                username=cur.fetchone()
                if username==None:   
                    messagebox. showerror("Error", f"Incorect Password or Username" ,parent=self.root)
                else: 
                    role=username[0]
                    if role=='Administrator' or role=='Accountant':
                        self.root.destroy ()
                        os.system("python3 Dashboard.py")
                    else:
                        self.root.destroy ()
                        os.system("python3 Billing.py")                 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

        
    def Forgot_Password(self):
        con = sqlite3.connect(database=r'employee.db')
        cur=con.cursor()
        try:
            if self.username.get()=="":
                 messagebox. showerror('Error', "Please enter your username" ,parent=self.root)
            else:
                cur.execute("select email from employee where id=? ",(self.username.get(),))
                mail=cur.fetchone()
                if mail==None:   
                    messagebox. showerror("Error", f"The username is invalid" ,parent=self.root)
                else: 
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.confirm_password=StringVar()
                    # call send_email_function ()
                    self.forget_window =Toplevel(self.root)
                    self.forget_window.title('RESET PASSWORD')
                    self.forget_window.geometry("500x400") 
                    self.forget_window.focus_force()
                    title=Label(self.forget_window,text="Reset Password",font=("montserrat",15, "bold"),fg="black")
                    title.pack(side= TOP,fill=X )
                    reset_passweord=Label(self.forget_window,text= "The OTP has been sent to your registerd email address",font=("montserrat",15, "bold"),fg="black")
                    reset_passweord.place(x=20,y=60)
                    box_reset_password=Entry(self.forget_window,textvariable=self.var_otp,font=("montserrat",15, "bold"),fg="black")
                    box_reset_password.place(x=30,y=100,width=300,height=40)
                    self.button_reset_password=Button(self.forget_window,text="Reset",font=("montserrat",15, "bold"),fg="black")
                    self.button_reset_password.place(x=350,y=100,width=100,height=40) 
                    
                    new_passweord=Label(self.forget_window,text= "New Password",font=("montserrat",15, "bold"),fg="black")
                    new_passweord.place(x=20,y=200)
                    New_password=Entry(self.forget_window,textvariable=self.var_new_password,font=("montserrat",15, "bold"),fg="black")
                    New_password.place(x=30,y=250,width=300,height=40)
                    
                    confirm_passweord=Label(self.forget_window,text= "Confirm Passwod",font=("montserrat",15, "bold"),fg="black")
                    confirm_passweord.place(x=20,y=300)
                    con_password=Entry(self.forget_window,textvariable=self.confirm_password,font=("montserrat",15, "bold"),fg="black")
                    con_password.place(x=30,y=350,width=300,height=40)
                    
                    self.button_submit=Button(self.forget_window,text="Submit",state=DISABLED,font=("montserrat",15, "bold"),fg="black")
                    self.button_submit.place(x=350,y=300,width=100,height=40)
                    
                    
                    
                    
                    
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)         


root = Tk()
obj = Login_System(root)
root.mainloop()
