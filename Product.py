import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox

class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.title("PocketBiz")
        self.root.geometry("1150x700+275+130")
        self.root.config(bg="#CADEED")
        self.root.focus_force()

        self.searchbar = LabelFrame(self.root, text="Search Product", font=("Roboto", 15, "bold"), bd=2, relief=RIDGE, bg="#CADEED", fg="#194569")

        
        #=====Variables=====
        self.searchby=StringVar()
        self.searchtxt=StringVar()
        self.ProductID=StringVar()
        self.Category=StringVar()
        self.category_list=[]
        self.Product=StringVar()
        self.Price=StringVar()
        self.Quantity=StringVar()
        self.Supplier=StringVar()
        self.supplier_list=[]
        self.Status=StringVar()
        self.get_info()

        self.label()
        self.entry()
        self.buttons()
        self.searchBar()
        self.searchBarOption()
        self.table()


        #=====Label=====
        
    def label(self) : 
        Category = Label(self.root,text="Category", font=("Roboto", 20, "bold"),bg="#CADEED")
        Category.place(x=30, y=140)
      
        Product = Label(self.root,text="Product ", font=("Roboto", 20, "bold"),bg="#CADEED")
        Product.place(x=400, y=140)
      
        Price = Label(self.root,text="Price", font=("Roboto", 20, "bold"),bg="#CADEED")
        Price.place(x=780, y=140)

        Quantity = Label(self.root,text="Quantity", font=("Roboto", 20, "bold"),bg="#CADEED")
        Quantity.place(x=30, y=250)
      
        Supplier = Label(self.root,text="Supplier ", font=("Roboto", 20, "bold"),bg="#CADEED")
        Supplier.place(x=400, y=250)
      
        Status = Label(self.root,text="Status", font=("Roboto", 20, "bold"),bg="#CADEED")
        Status.place(x=780, y=250)

        
        #=====Entry=====
    def entry(self) : 
        search_Category = ttk.Combobox(self.root,textvariable=self.Category, values=self.category_list, state="readonly", justify=CENTER, font=("Roboto", 15))
        search_Category.current(0)
        search_Category.place(x=150, y=140, width=180)
        
        Product_Txt = Entry(self.root,textvariable=self.Product, font=("Roboto", 15),bd=2)
        Product_Txt.place(x=500, y=140, width=180)
      
        Price_Txt = Entry(self.root,textvariable=self.Price, font=("Roboto", 15),bd=2)
        Price_Txt.place(x=850, y=140, width=180)
        
        Quantity_Txt = Entry(self.root,textvariable=self.Quantity, font=("Roboto", 15),bd=2)
        Quantity_Txt.place(x=150, y=250, width=180)
      
        search_Supplier = ttk.Combobox(self.root,textvariable=self.Supplier, values=self.supplier_list, state="readonly", justify=CENTER, font=("Roboto", 15))
        search_Supplier.current(0)
        search_Supplier.place(x=500, y=250, width=180)
        
        search_Status = ttk.Combobox(self.root,textvariable=self.Status, values=("Select","Active","Inactive"), state="readonly", justify=CENTER, font=("Roboto", 15))
        search_Status.current(0)
        search_Status.place(x=850, y=250, width=180)
      
        #====Buttons====
    def buttons(self) : 
        buttons = [
        {"text": "Save", "command": self.save, "x": 350, "y": 350 , "width": 105, "bg": "#152238", "cursor": "hand1"},
        {"text": "Update", "command": self.update, "x": 455, "y": 350, "width": 105, "bg": "#8B8000", "cursor": "hand1"},
        {"text": "Delete", "command": self.delete, "x": 560, "y": 350, "width": 105, "bg": "#880808", "cursor": "hand1"},
        {"text": "Clear", "command": self.clear, "x": 665 , "y": 350, "width": 105, "bg": "#023020", "cursor": "hand1"}
        ]

        
        for button in buttons:
            b = Button(self.root,text=button["text"], command=button["command"], font=("Roboto", 15), bg=button["bg"], cursor=button["cursor"])
            b.place(x=button["x"], y=button["y"], width=button["width"])
            
        
        # Search Bar
    def searchBar(self) : 
        self.searchbar.place(x=250, y=10, width=600, height=80)

        # Search Bar Options
    def searchBarOption(self) : 
        search_bar = ttk.Combobox(self.searchbar, textvariable=self.searchby, values=("Select", "Supplier", "Product","Category"), state="readonly", justify=CENTER, font=("Roboto", 15))
        search_bar.current(0)
        search_bar.place(x=10, y=10, width=180)

        option_bar = Entry(self.searchbar, textvariable=self.searchtxt, font=("Roboto", 15))
        option_bar.place(x=200, y=9, width=180)

        search_button = Button(self.searchbar, text="Search", command=self.search, font=("Roboto", 15), bg="#FFFF00", cursor="hand2")
        search_button.place(x=400, y=9, width=180)
        
        #====Table====
    def table(self):
        table = Frame(self.root, bd=3, relief=RIDGE) 
        table.place(x=0, y=400, width=1150, height=350)
        vertical_scroll = Scrollbar(table, orient=VERTICAL)
        horizontal_scroll = Scrollbar(table, orient=HORIZONTAL)
        self.table = ttk.Treeview(table, columns=("pid", "category", "product", "price", "quantity", "supplier", "status"), yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set)
        
        headings = [
        ("pid", "Product ID"),
        ("category", "Category"),
        ("product", "Product"),
        ("price", "Price"),
        ("quantity", "Quantity"),
        ("supplier", "Supplier"),
        ("status", "Status"),
        ]
        
        for heading in headings:
         self.table.heading(heading[0], text=heading[1])
        
        self.table["show"] = "headings"
        
        self.table.column("pid", width=100)
        self.table.column("category", width=100)
        self.table.column("product", width=100)
        self.table.column("price", width=100)
        self.table.column("quantity", width=100)
        self.table.column("supplier", width=100)
        self.table.column("status", width=100)
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease - 1 >", self.table_click)

        vertical_scroll.pack(side=BOTTOM, fill=X)
        horizontal_scroll.pack(side=RIGHT, fill=Y)
        vertical_scroll.config(command=self.table.yview)
        horizontal_scroll.config(command=self.table.xview)
        self.Show() 
        
            
    def get_info(self):
        con = sqlite3.connect(database=r"employee.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            categories=cur.fetchall()
            self.category_list.append("Empty")
            if len(categories)>0:
                del self.category_list[:]
                self.category_list.append("Select")
                for i in categories:
                    self.category_list.append(i[0])
            cur.execute("SELECT name FROM supplier")
            suppliers=cur.fetchall()
            self.supplier_list.append("Empty")
            if len(suppliers)>0:
                del self.supplier_list[:]
                self.supplier_list.append("Select")
                for i in suppliers:
                    self.supplier_list.append(i[0])
            
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
    
    def save(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      category = self.Category.get()
      product=self.Product.get()
      price = self.Price.get()
      quantity = self.Quantity.get()
      supplier = self.Supplier.get()
      status=self.Status.get()

      if self.Category.get() == "Select" or self.Product.get() == "" or self.Price.get() == "" or self.Quantity.get() == "" or self.Supplier.get() == "Select" or self.Status.get() == "Select":
       messagebox.showerror("Error", "Please enter the required information in the fields", parent=self.root)
       return

      cur.execute("SELECT * FROM product WHERE supplier=? AND product=? AND category=?", (self.Supplier.get(), self.Product.get(), self.Category.get()))
      row = cur.fetchone()

      if row:
         messagebox.showerror("Error", f"{product} already exists", parent=self.root)
      else:
         cur.execute("""
            INSERT INTO product (category, product, price, quantity, supplier, status)
            VALUES (?,?,?,?,?,?)
        """,(category, product, price, quantity, supplier, status))
         con.commit()
         messagebox.showinfo("Success", f"{product} saved successfully", parent=self.root)
         self.Show()
      con.close()

   #====Shows all the values inputed in the employee menu====  
    def Show(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
         cur.execute("SELECT * FROM product")
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
         self.ProductID.set(values[0])
         self.Category.set(values[1])
         self.Product.set(values[2])
         self.Price.set(values[3])
         self.Quantity.set(values[4])
         self.Supplier.set(values[5])
         self.Status.set(values[6])   
   
    def update(self):
        con = sqlite3.connect(database=r"employee.db")
        cur = con.cursor()

        if not self.ProductID.get():
            messagebox.showerror("Error", "Please select the product from the list", parent=self.root)
            return

        cur.execute("SELECT * FROM product WHERE pid=?;", (self.ProductID.get(),))
        row = cur.fetchone()
        if not row:
            messagebox.showerror("Error", f"Product with ProductID {self.ProductID.get()} cannot be updated as it does not exist", parent=self.root)
            return

        try:
            cur.execute("UPDATE product SET category=?, product=?, price=?, quantity=?, supplier=?, status=? WHERE pid=?;",
                    (self.Category.get(), self.Product.get(), self.Price.get(), self.Quantity.get(), self.Supplier.get(), self.Status.get(), self.ProductID.get()))
            con.commit()
            messagebox.showinfo("Success", f"Product with ProductID {self.ProductID.get()} updated successfully", parent=self.root)
            self.Show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        cur.close()
        con.close()

       
    def delete(self):
        con = sqlite3.connect(database=r"employee.db")
        cur = con.cursor()
        try:
            if self.ProductID.get() == "":
                messagebox.showerror("Error", f"Please enter the ProductID number", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?;", (self.ProductID.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", f"Product with ProductID {self.ProductID.get()} cannot be updated as there is no value entered previously", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {self.Product.get()}?", parent=self.root)
                    if option:
                        cur.execute("Delete from product where pid=?",(self.ProductID.get(),))
                        con.commit()
                        messagebox.showinfo("Success", f"{self.Product.get()} deleted successfully", parent=self.root) 
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=self.root)


    def clear(self):
      values = [" ", " ", " ", " ", " ", " "]
      vars = [self.Category, self.Product, self.Price, self.Quantity,
            self.Supplier, self.Status]
      for var, value in zip(vars, values):
         var.set(value)

      self.searchby.set("Select")
      self.searchtxt.set(" ")
      self.Show()   
   
    def search(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      search_by = self.searchby.get()
      search_txt = self.searchtxt.get()

      if search_by == "Select":
         messagebox.showerror("Error", "Select search by option", parent=self.root)
         return
      elif not search_txt:
         messagebox.showerror("Error", "Please enter search criteria", parent=self.root)
         return

      try:
         query = f"SELECT * from product WHERE {search_by} LIKE ?"
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
   object=ProductClass(root)
   root.mainloop()    