import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox

class EmployeeClass:
   def __init__(self, root):
      self.root = root
      self.root.title("PocketBiz")
      self.root.geometry("1150x700+275+130")
      self.root.config(bg="#CADEED")
      self.root.focus_force()

      self.searchbar = LabelFrame(self.root, text="Search Employee", font=("Roboto", 15, "bold"), bd=2, relief=RIDGE, bg="#CADEED", fg="#000000")


      vars_ = [("employee_searchby", StringVar()),
      ("employee_searchtxt", StringVar()),
      ("employee_id", StringVar()),
      ("employee_name", StringVar()),
      ("employee_email", StringVar()),
      ("employee_contact", StringVar()),
      ("employee_password", StringVar()),
      ("employee_role", StringVar()),
      ("employee_dob", StringVar()),
      ("employee_gender", StringVar()),
      ("employee_address", StringVar()),
      ("employee_salary", StringVar()),
      ("employee_status", StringVar())]
      for var in vars_:
         setattr(self, *var)

      self.searchBar()
      self.searchBarOptions()
      self.bar()
      self.buttons()
      self.table()

         
      # Search Bar
   def searchBar(self) : 
      self.searchbar.place(x=250, y=20, width=600, height=70)

      # Search Bar Options
   def searchBarOptions(self) : 
      search_bar = ttk.Combobox(self.searchbar, textvariable=self.employee_searchby, values=("Select", "Name", "Email", "Contact", "ID"), state="readonly", justify=CENTER, font=("Roboto", 15))
      search_bar.current(0)
      search_bar.place(x=10, y=10, width=180)

      option_bar = Entry(self.searchbar, textvariable=self.employee_searchtxt, font=("Roboto", 15), bg="#FFE5B4")
      option_bar.place(x=200, y=9, width=180)

      search_button = Button(self.searchbar, text="Search", command=self.search, font=("Roboto", 15), bg="#FFFF00", cursor="hand2")
      search_button.place(x=400, y=9, width=180)

      # Bar
   def bar(self) : 
      bar = Label(self.root, text="Employee Details", font=("Roboto", 15, "bold"), bd=2, bg="#194569", fg="#FFFFFF")
      bar.place(x=50, y=100, width=1000)
      
      #====Bar Options====
      options = [
      ("ID", "ID", 50, 250),
      ("Name", "Name", 50, 150),
      ("Email", "Email", 425, 150),
      ("Contact", "Contact", 750, 150),
      ("Password", "Password", 425, 250),
      ("Role", "Role", 750, 250),
      ("D.O.B", "D.O.B", 50, 350),
      ("Gender", "Gender", 425, 350),
      ("Address", "Address", 750, 350),
      ("Salary", "Salary", 50, 450),
      ("Status", "Status", 425, 450),
      ]

      for option in options:
         Label(self.root, text=option[0], font=("Roboto", 15, "bold"), bd=2, bg="#CADEED").place(x=option[2], y=option[3])

      #====Writing space for the Bar Options====
      entry_options = [
      (self.employee_id, "txtid_bar", 125, 250, 180),
      (self.employee_name, "txt_name_bar", 125, 150, 180),
      (self.employee_email, "txtemail_bar", 530, 150, 155),
      (self.employee_contact, "txtconatact_bar", 850, 150, 180),
      (self.employee_password, "txtpassword_bar", 530, 250, 155),
      (self.employee_dob, "txtdob_bar", 125, 350, 180),
      (self.employee_address, "txtaddress_bar", 850, 350, 180),
      (self.employee_salary, "txtsalary_bar", 125, 450, 180),
      ]

      for entry_option in entry_options:
         Entry(self.root, textvariable=entry_option[0], font=("Roboto", 15, "bold"), bd=2, bg="#FFFFFF").place(x=entry_option[2], y=entry_option[3], width=entry_option[4])

      search_role = ttk.Combobox(self.root, textvariable=self.employee_role, values=("Select","Administrator","Shopkeeper","Accountant"), state="readonly", justify=CENTER, font=("Roboto", 15,"bold"))
      search_role.current(0)
      search_role.place(x=850, y=250, width=180)

      search_gender = ttk.Combobox(self.root, textvariable=self.employee_gender, values=("Select","Male","Female","Other"), state="readonly", justify=CENTER, font=("Roboto", 15,"bold"))
      search_gender.current(0)
      search_gender.place(x=530, y=350, width=155)
      
      search_status = ttk.Combobox(self.root, textvariable=self.employee_status, values=("Select","Paid","Unpaid"), state="readonly", justify=CENTER, font=("Roboto", 15,"bold"))
      search_status.current(0)
      search_status.place(x=530, y=450, width=155)

      
      #====Buttons====
   def buttons(self) : 
      buttons = [
      {"text": "Save", "command": self.save, "x": 400, "y": 500, "width": 100, "bg": "#152238", "cursor": "hand1"},
      {"text": "Update", "command": self.update, "x": 500, "y": 500, "width": 100, "bg": "#8B8000", "cursor": "hand1"},
      {"text": "Delete", "command": self.delete, "x": 600, "y": 500, "width": 100, "bg": "#880808", "cursor": "hand1"},
      {"text": "Clear", "command": self.clear, "x": 700, "y": 500, "width": 100, "bg": "#023020", "cursor": "hand1"}
        ]
        
      for button in buttons:
         b = Button(self.root, text=button["text"], command=button["command"], font=("Roboto", 15), bg=button["bg"], cursor=button["cursor"])
         b.place(x=button["x"], y=button["y"], width=button["width"])
        
      #====Table====
   def table(self) : 
      table = Frame(self.root, bd=3, relief=RIDGE) 
      table.place(x=0, y=550, relwidth=1, height=150)
      vertical_scroll = Scrollbar(table, orient=VERTICAL)
      horizontal_scroll = Scrollbar(table, orient=HORIZONTAL)
      self.table = ttk.Treeview(table, columns=("id", "name", "email", "contact", "password", "role", "dob", "gender", "address", "salary", "status"), yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set)
        
      headings = [
         ("id", "ID"),
         ("name", "Name"),
         ("email", "Email"),
         ("contact", "Contact"),
         ("password", "Password"),
         ("role", "Role"),
         ("dob", "DOB"),
         ("gender", "Gender"),
         ("address", "Address"),
         ("salary", "Salary"),
         ("status", "Salary Status")
        ]
        
      for heading in headings:
         self.table.heading(heading[0], text=heading[1])
        
      self.table["show"] = "headings"
        
      self.table.column("id", width=100)
      self.table.column("name", width=100)
      self.table.column("email", width=100)
      self.table.column("contact", width=100)
      self.table.column("password", width=100)
      self.table.column("role", width=100)
      self.table.column("dob", width=100)
      self.table.column("gender", width=100)
      self.table.column("address", width=100)
      self.table.column("salary", width=100)
      self.table.column("status", width=100) 
      self.table.pack(fill=BOTH, expand=1)
      self.table.bind("<ButtonRelease - 1 >", self.table_click)

      vertical_scroll.pack(side=BOTTOM, fill=X)
      horizontal_scroll.pack(side=RIGHT, fill=Y)
      vertical_scroll.config(command=self.table.yview)
      horizontal_scroll.config(command=self.table.xview)
      self.Show() 
      
   def save(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      id = self.employee_id.get()
      name = self.employee_name.get()
      email = self.employee_email.get()
      contact = self.employee_contact.get()
      password = self.employee_password.get()
      role = self.employee_role.get()
      dob = self.employee_dob.get()
      gender = self.employee_gender.get()
      address = self.employee_address.get()
      salary = self.employee_salary.get()
      status = self.employee_status.get()
      
      try:
        int(id)
      except ValueError:
        messagebox.showerror("Error","Invalid id. Please enter an integer value.",parent=self.root)
        return
      

      if not id:
         messagebox.showerror("Error", "Please enter employee id", parent=self.root)
         return
      

      cur.execute("SELECT * FROM employee WHERE id=?", (id,))
      row = cur.fetchone()

      if row:
         messagebox.showerror("Error", f"Employee with id {id} already exists", parent=self.root)
      else:
         cur.execute("""
            INSERT INTO employee (id, name, email, contact, password, role, dob, gender, address, salary, status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
         """, (id, name, email, contact, password, role, dob, gender, address, salary, status))
         con.commit()
         messagebox.showinfo("Success", f"Employee with id {id} saved successfully", parent=self.root)
         self.Show()
      con.close()

         
   #====Shows all the values inputed in the employee menu====  
   def Show(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
         cur.execute("SELECT * FROM employee")
         rows = cur.fetchall()
         self.table.delete(*self.table.get_children())
         if rows:
            for row in rows:
               self.table.insert("", END, values=row)
         else:
            ()
      except Exception as ex:
         messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
   
   #====function implmented when the table is clicked =====
   def table_click(self, event):
      selected_item = self.table.focus()
      if selected_item:
         values = self.table.item(selected_item)["values"]
         self.employee_id.set(values[0])
         self.employee_name.set(values[1])
         self.employee_email.set(values[2])
         self.employee_contact.set(values[3])
         self.employee_password.set(values[4])
         self.employee_role.set(values[5])
         self.employee_dob.set(values[6])
         self.employee_gender.set(values[7])
         self.employee_address.set(values[8])
         self.employee_salary.set(values[9])
         self.employee_status.set(values[10])   
      
   def update(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
        int(id)
      except ValueError:
        messagebox.showerror("Error","Invalid id. Please enter an integer value.",parent=self.root)
        return 
      
      if not self.employee_id.get():
         messagebox.showerror("Error", "Please enter employee id", parent=self.root)
         return
    
      cur.execute("SELECT * FROM employee WHERE id=?;", (self.employee_id.get(),))
      row = cur.fetchone()
      if not row:
         messagebox.showerror("Error", f"Employee with id {self.employee_id.get()} cannot be updated as there is no value entered previously", parent=self.root)
         return
      
      try:
         cur.execute("UPDATE employee SET name=?, email=?, contact=?, password=?, role=?, dob=?, gender=?, address=?, salary=?, status=? WHERE id=?",
         (self.employee_name.get(), self.employee_email.get(), self.employee_contact.get(), self.employee_password.get(), self.employee_role.get(), self.employee_dob.get(), self.employee_gender.get(), self.employee_address.get(), self.employee_salary.get(), self.employee_status.get(), self.employee_id.get()))
         con.commit()
         messagebox.showinfo("Success", f"Employee with id {self.employee_id.get()} updated successfully", parent=self.root)
         self.Show() 
      except Exception as ex:
         messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

   
   def delete(self):
      con=sqlite3.connect(database=r"employee.db")
      cur=con.cursor()
      
      try:
         if self.employee_id.get()=="":
            messagebox.showerror("Error",f"Please enter employee id",parent=self.root)
         else:
            cur.execute("Select * from employee where id=?;",(self.employee_id.get(),))
            row=cur.fetchone()
            if row == None:
               messagebox.showerror("Error",f"Employee with id {self.employee_id.get()} cannot be updated as there is no value entered previously",parent=self.root)
            else:
               option=messagebox.askyesno("Confirmation",f"Are you sure you want to delete {self.employee_name.get()}?",parent=self.root)
               if option == True:
                  cur.execute("Delete from employee where id =?",(self.employee_id.get(),))
                  con.commit()
                  messagebox.showinfo("Success",f"Employee with id {self.employee_id.get()} deleted successfully",parent=self.root) 
                  self.clear()
      except Exception as ex:
         messagebox.showerror("Error",f" Error due to :{str(ex)}",parent=self.root)
               
   def clear(self):
      values = [" ", " ", " ", " ", " ", "Admin", " ", "Select", " ", " ", " "]
      vars = [self.employee_id, self.employee_name, self.employee_email, self.employee_contact,
            self.employee_password, self.employee_role, self.employee_dob, self.employee_gender,
            self.employee_address, self.employee_salary, self.employee_status]
      for var, value in zip(vars, values):
         var.set(value)

      self.employee_searchby.set("Select")
      self.employee_searchtxt.set(" ")
      self.Show()   

         
   def search(self):

      try : 
      
         con = sqlite3.connect(database=r"employee.db")
         cur = con.cursor()
         search_by = self.employee_searchby.get()
         search_txt = self.employee_searchtxt.get()

         if search_by == "Select":
            messagebox.showerror("Error", "Select search by option", parent=self.root)
            return
         elif not search_txt:
            messagebox.showerror("Error", "Please enter search criteria", parent=self.root)
            return

         try:
            query = f"SELECT * from employee WHERE {search_by} LIKE '%{search_txt}%'"
            cur.execute(query)
            rows = cur.fetchall()

            if rows:
               self.table.delete(*self.table.get_children())
               for row in rows:
                  self.table.insert("", END, values=row)
            else:
               messagebox.showerror("Error", "No records found", parent=self.root)
         except Exception as ex:
            messagebox.showerror("Error", "Error due to: " + str(ex), parent=self.root)

      except : 
         messagebox.showerror("Error", "Wrong name", parent= self.root)
               
      
if __name__ == "__main__":
   root=Tk()
   object=EmployeeClass(root)
   root.mainloop()  