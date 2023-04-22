import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox

class SupplierClass:
   def __init__(self, root):
      self.root = root
      self.root.title("PocketBiz")
      self.root.geometry("1150x700+275+130")
      self.root.config(bg="#CADEED")
      self.root.focus_force()

      

      vars_ = [("supplier_searchby", StringVar()),
      ("supplier_searchtxt", StringVar()),
      ("supplier_invoice", StringVar()),
      ("supplier_name", StringVar()),
      ("supplier_email", StringVar()),
      ("supplier_contact", StringVar()),
      ("supplier_password", StringVar()),
      ("supplier_role", StringVar()),
      ("supplier_dob", StringVar()),
      ("supplier_gender", StringVar()),
      ("supplier_address", StringVar()),
      ("supplier_salary", StringVar()),
      ("supplier_status", StringVar())]
      
      for var in vars_:
         setattr(self, *var)

      self.searchBar()
      self.bar()
      self.buttons()
      self.table()
      
      # Search Bar
   def searchBar(self) : 
      searchbar = LabelFrame(self.root, text="Search Supplier", font=("Roboto", 15, "bold"), bd=2, relief=RIDGE, bg="#CADEED", fg="#000000")
      searchbar.place(x=250, y=20, width=600, height=70)

      # Search Bar Options
      search_bar = ttk.Combobox(searchbar, textvariable=self.supplier_searchby, values=("Select", "Name", "Email", "Contact"), state="readonly", justify=CENTER, font=("Roboto", 15))
      search_bar.current(0)
      search_bar.place(x=10, y=10, width=180)

      option_bar = Entry(searchbar, textvariable=self.supplier_searchtxt, font=("Roboto", 15), bg="#FFE5B4")
      option_bar.place(x=200, y=9, width=180)

      search_button = Button(searchbar, text="Search", command=self.search, font=("Roboto", 15), bg="#FFFF00", cursor="hand2")
      search_button.place(x=400, y=9, width=180)

      # Bar
   def bar(self) : 
      bar = Label(self.root, text="Supplier Details", font=("Roboto", 15, "bold"), bd=2, bg="#194569", fg="#FFFFFF")
      bar.place(x=50, y=100, width=1000)
      
      #====Bar Options====
      options = [
      ("Invoice No", "Invoice", 100, 150),
      ("Name", "Name", 450, 150),
      ("Email", "Email", 750, 150),
      ("Contact", "Contact", 260, 220),
      ("Address", "Address", 650, 220),
      ]

      for option in options:
         Label(self.root, text=option[0], font=("Roboto", 15, "bold"), bd=2, bg="#CADEED").place(x=option[2], y=option[3])

      #====Writing space for the Bar Options====
      entry_options = [
      (self.supplier_invoice, "txtid_bar", 200, 150, 180),
      (self.supplier_name, "txt_name_bar", 520, 150, 180),
      (self.supplier_email, "txtemail_bar", 820, 150, 180),
      (self.supplier_contact, "txtconatact_bar", 340, 220, 180),
      (self.supplier_address, "txtaddress_bar", 730, 220, 180),
      ]
      
      for entry_option in entry_options:
         Entry(self.root, textvariable=entry_option[0], font=("Roboto", 15, "bold"), bd=2, bg="#FFFFFF").place(x=entry_option[2], y=entry_option[3], width=entry_option[4])
         
      #====Buttons====
   def buttons(self) : 
      buttons = [
      {"text": "Save", "command": self.save, "x": 370, "y": 300, "width": 100, "bg": "#152238", "cursor": "hand1"},
      {"text": "Update", "command": self.update, "x": 470, "y": 300, "width": 100, "bg": "#8B8000", "cursor": "hand1"},
      {"text": "Delete", "command": self.delete, "x": 570, "y": 300, "width": 100, "bg": "#880808", "cursor": "hand1"},
      {"text": "Clear", "command": self.clear, "x": 670, "y": 300, "width": 100, "bg": "#023020", "cursor": "hand1"}
        ]
      
      for button in buttons:
         b = Button(self.root, text=button["text"], command=button["command"], font=("Roboto", 15), bg=button["bg"], cursor=button["cursor"])
         b.place(x=button["x"], y=button["y"], width=button["width"])
         
      #====Table====
   def table(self) : 
      table = Frame(self.root, bd=3, relief=RIDGE) 
      table.place(x=0, y=350, height=350, width=1150)
      vertical_scroll = Scrollbar(table, orient=VERTICAL)
      horizontal_scroll = Scrollbar(table, orient=HORIZONTAL)
      self.table = ttk.Treeview(table, columns=("supplier_invoice", "name", "email", "contact","address"), yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set)
        
      headings = [
         ("supplier_invoice", "Invoice No"),
         ("name", "Name"),
         ("email", "Email"),
         ("contact", "Contact"),
         ("address", "Address"),
        ]
      
      for heading in headings:
         self.table.heading(heading[0], text=heading[1])
      
      self.table["show"] = "headings"
        
      self.table.column("supplier_invoice", width=100)
      self.table.column("name", width=100)
      self.table.column("email", width=100)
      self.table.column("contact", width=100)
      self.table.column("address", width=100) 
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
      supplier_invoice = self.supplier_invoice.get()
      name = self.supplier_name.get()
      email = self.supplier_email.get()
      contact = self.supplier_contact.get()
      address = self.supplier_address.get()

      if not supplier_invoice:
         messagebox.showerror("Error", "Please enter the supplier invoice number", parent=self.root)
         return
      cur.execute("SELECT * FROM supplier WHERE supplier_invoice=?", (supplier_invoice,))
      row = cur.fetchone()

      if row:
         messagebox.showerror("Error", f"Supplier with invoice {supplier_invoice} already exists", parent=self.root)
      else:
         cur.execute("""
            INSERT INTO supplier (supplier_invoice, name, email, contact, address)
            VALUES (?,?,?,?,?)
        """,(supplier_invoice, name, email, contact, address))
         con.commit()
         messagebox.showinfo("Success", f"Supplier with invoice {supplier_invoice} saved successfully", parent=self.root)
         self.Show()
      con.close()

   #====Shows all the values inputed in the employee menu====  
   def Show(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
         cur.execute("SELECT * FROM supplier")
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
         self.supplier_invoice.set(values[0])
         self.supplier_name.set(values[1])
         self.supplier_email.set(values[2])
         self.supplier_contact.set(values[3])
         self.supplier_address.set(values[4])   
   
   def update(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()

      if not self.supplier_invoice.get():
         messagebox.showerror("Error", "Please enter the invoice number", parent=self.root)
         return

      cur.execute("SELECT * FROM supplier WHERE supplier_invoice=?;", (self.supplier_invoice.get(),))
      row = cur.fetchone()
      if not row:
         messagebox.showerror("Error", f"Supplier with invoice {self.supplier_invoice.get()} cannot be updated as it does not exist", parent=self.root)
         return

      try:
         cur.execute("UPDATE supplier SET name=?, email=?, contact=?, address=? WHERE supplier_invoice=?;",
                    (self.supplier_name.get(), self.supplier_email.get(), self.supplier_contact.get(), self.supplier_address.get(), self.supplier_invoice.get()))
         con.commit()
         messagebox.showinfo("Success", f"Supplier with invoice {self.supplier_invoice.get()} updated successfully", parent=self.root)
         self.Show()
      except Exception as ex:
         messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
       
   def delete(self):
      con=sqlite3.connect(database=r"employee.db")
      cur=con.cursor()
      try:
         if self.supplier_invoice.get()=="":
            messagebox.showerror("Error",f"Please enter supplier invoice number",parent=self.root)
         else:
            cur.execute("Select * from supplier where supplier_invoice=?;",(self.supplier_invoice.get(),))
            row=cur.fetchone()
            if row == None:
               messagebox.showerror("Error",f"Supplier with invoice number{self.supplier_invoice.get()} cannot be updated as there is no value entered previously",parent=self.root)
            else:
               option=messagebox.askyesno("Confirmation",f"Are you sure you want to delete {self.supplier_name.get()}?",parent=self.root)
               if option == True:
                  cur.execute("Delete from supplier where supplier_invoice=?",(self.supplier_invoice.get(),))
                  con.commit()
                  messagebox.showinfo("Success",f"Supplier with invoice number {self.supplier_invoice.get()} deleted successfully",parent=self.root) 
                  self.clear()
      except Exception as ex:
         messagebox.showerror("Error",f" Error due to :{str(ex)}",parent=self.root)

   def clear(self):
      values = [" ", " ", " ", " ", " "]
      vars = [self.supplier_invoice, self.supplier_name, self.supplier_email, self.supplier_contact,
            self.supplier_address]
      for var, value in zip(vars, values):
         var.set(value)

      self.supplier_searchby.set("Select")
      self.supplier_searchtxt.set(" ")
      self.Show()   
   
   def search(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      search_by = self.supplier_searchby.get()
      search_txt = self.supplier_searchtxt.get()

      if search_by == "Select":
         messagebox.showerror("Error", "Select search by option", parent=self.root)
         return
      elif not search_txt:
         messagebox.showerror("Error", "Please enter search criteria", parent=self.root)
         return

      try:
         query = f"SELECT * from supplier WHERE {search_by} LIKE ?"
         cur.execute(query, ('%' + search_txt + '%',))
         rows = cur.fetchall()

         if rows:
            self.table.delete(*self.table.get_children())
            for row in rows:
               self.table.insert("", END, values=row)
         else:
            messagebox.showerror("Error", "No records found", parent=self.root)
      except Exception as ex:
         messagebox.showerror("Error", "Error due to: " + str(ex), parent=self.root) 
 
         
if __name__ == "__main__":
   root=Tk()
   object=SupplierClass(root)
   root.mainloop()    