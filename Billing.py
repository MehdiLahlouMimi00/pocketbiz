import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import time
import os
import tempfile
 
class billing:
    def __init__(self, root):
      self.root = root
      self.root.title("PocketBiz")
      self.root.geometry("1450x800")
      self.root.config(bg="#CADEED")
      self.root.resizable(False, False)

      x = (root.winfo_screenwidth() / 2) - (1450 / 2)
      y = (root.winfo_screenheight() / 2) - (800 / 2) 

      self.Cal_Cart_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
                                                           
      self.root.geometry(f"+{int(x)}+{int(y)}")
      self.cart_list=[]
      self.chk_print=0

      self.createTitle()
      self.createLogout()
      self.createClock()
      self.createProductFrame()
      self.customerFrame()
      self.bill()
      self.addToCart()

      #====Title====
    def createTitle(self) : 
        self.icon_title = Image.open("images/LOGO.png")
        self.icon_title = self.icon_title.resize((50, 50), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        self.title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon_title, compound=LEFT, font=("roboto", 40, "bold"), bg="#194569", fg="white", anchor="w", padx=20)
        self.title.place(x=0, y=0, relwidth=1, height=70)
        
      #====Logout_Button====
    def createLogout(self) : 
        Logout_Button = Button(self.root, text="LOGOUT",command=self.Logout,font=("roboto", 15), cursor="hand2")
        Logout_Button.place(x=1200, y=15, height=50, width=150)
        
      #====Clock====
    def createClock(self) :
        self.clock = Label(self.root, text="Welcome to PocketBiz\t\t\t Date: DD-MM-YYYY\t\t\t Time: HH:MM:SS ", font=("roboto", 15), bg="#194569", fg="white")
        self.clock.place(x=0, y=70, relwidth=1, height=30)
        
     #====Product Frames===
    def createProductFrame(self) : 
        self.variable_search= StringVar() 
        ProductFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        ProductFrame.place(x=6, y=110, width=450, height=680)

        Product_Title = Label(ProductFrame, text="All Products", font=("Roboto", 20, "bold"), bg="#262626", fg="white")
        Product_Title.pack(side=TOP, fill=X)
      
        ProductTable = Frame(ProductFrame, bd=3, relief=RIDGE)
        ProductTable.place(x=2, y=37, width=435 , height=625)
        scrolly = Scrollbar(ProductTable, orient=VERTICAL)
        scrollx = Scrollbar(ProductTable, orient=HORIZONTAL)
        self.Product_Table = ttk.Treeview(ProductTable, columns=("id", "category", "product", "price", "quantity"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)
        self.Product_Table.heading("id", text="ID")
        self.Product_Table.heading("category", text="Category")
        self.Product_Table.heading("product", text="Product")
        self.Product_Table.heading("price", text="Price")
        self.Product_Table.heading("quantity", text="Quantity")
        self.Product_Table["show"] = "headings"
        self.Product_Table.column("id", width=50)
        self.Product_Table.column("category", width=120)
        self.Product_Table.column("product", width=70)
        self.Product_Table.column("price", width=60)
        self.Product_Table.column("quantity", width=80)
        self.Product_Table.pack(fill=BOTH, expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)

        Ibl_note = Label(ProductTable, text="'", font=("times new roman", 10), bg="white", fg="red")
        Ibl_note.pack(side=BOTTOM, fill=X)

      #===Customer Frame===
    def customerFrame(self) : 
        self.var_CustomerName = StringVar()
        self.var_contact = StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=460, y=110, width=530, height=70)

        CustomerTitle = Label(CustomerFrame, text="Customer Details", font=("Roboto", 20, "bold"), bg="#262626", fg="white")
        CustomerTitle.pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=10, y=35)

        txt_name = Entry(CustomerFrame, textvariable=self.var_CustomerName, font=("times new roman", 12, "bold"), bg="lightyellow")
        txt_name.place(x=55, y=37, width=200, height=22)

        lbl_contact = Label(CustomerFrame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        lbl_contact.place(x=260, y=35)

        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 12, "bold"), bg="lightyellow")
        txt_contact.place(x=320, y=37, width=200, height=22)

        
        self.Cal_Cart_Frame.place(x=460, y=185, width=530, height=490)

      #bill
    def bill(self) : 
        cart_Frame = Frame(self.Cal_Cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=10, y=10, width=500, height=460)
        self.cartTitle = Label(cart_Frame, text="Cart  \t  Total Product: [0]", font=("times new roman", 15))
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame, columns=("id", "name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("id", text="ID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="Quantity") 
        self.CartTable["show"] = "headings"
        self.CartTable.column("id", width=50)
        self.CartTable.column("name", width=120)
        self.CartTable.column("price", width=70)
        self.CartTable.column("qty", width=60)
        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
 
      #===ADD To Cart Button====
    def addToCart(self) : 
        self.var_pid = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=460, y=680, width=530, height=110)

        lbl_P_name = Label(Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white")
        lbl_P_name.place(x=5, y=5)

        txt_P_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_name, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_P_name.place(x=5, y=35, width=190, height=22)

        lbl_P_price = Label(Add_CartWidgetsFrame, text="Price", font=("times new roman", 15), bg="white")
        lbl_P_price.place(x=210, y=5)

        txt_P_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_P_price.place(x=210, y=35, width=150, height=22)

        lbl_P_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white")
        lbl_P_qty.place(x=370, y=5)

        txt_P_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15), bg="lightyellow")
        txt_P_price.place(x=370, y=35, width=150, height=22)

        self.lbl_inStock = Label(Add_CartWidgetsFrame, text="In Stock", font=("times new roman", 20), bg="white")
        self.lbl_inStock.place(x=5, y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame, text="Clear",command=self.clear_cart,font=("times new roman", 15, "bold"),bg="lightgray", cursor="hand2")
        btn_clear_cart.place(x=140,y=70,width=170,height=30)

        btn_add_cart=Button(Add_CartWidgetsFrame, text="Add | Update ",command=self.add_update_cart,font=("times new roman", 15, "bold"),bg="orange", cursor="hand2")
        btn_add_cart.place(x=330,y=70,width=170,height=30)
      
     #===billing area===
    def billing(self) : 
      billFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
      billFrame.place(x=995, y=110, width=450, height=530)

      bTitle = Label(billFrame, text="Customer Bill Area", font=("Roboto", 20, "bold"), bg="black", fg="white")
      bTitle.pack(side=TOP, fill=X)

      scrolly = Scrollbar(billFrame, orient=VERTICAL)
      scrolly.pack(side=RIGHT, fill=Y)

      self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
      self.txt_bill_area.pack(fill=BOTH, expand=1)

      scrolly.config(command=self.txt_bill_area.yview)
       #===BIlling Button===
      billMenuFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
      billMenuFrame.place(x=995, y=645, width=450, height=145)
    
      
      self.lbl_amnt=Label(billMenuFrame, text= 'Bill Amount \n [0]', font=("Times new roman", 15, "bold"),bg="#FD0100", fg="white")
      self.lbl_amnt.place(x=0,y=0, width=148, height=70)
      
      self.lbl_discount=Label(billMenuFrame, text= 'Discount \n [5%]', font=("Times new roman", 15, "bold"),bg="#F76915", fg="white")
      self.lbl_discount.place(x=147,y=0, width=148, height=70)
      
      self.lbl_net_pay=Label(billMenuFrame, text= 'Net Pay \n [0]', font=("Times new roman", 15, "bold"),bg="#EEDE04", fg="white")
      self.lbl_net_pay.place(x=295,y=0, width=148, height=70)
      
      btn_print=Button(billMenuFrame, text= 'Print',command=self.print_bill,  font=("Times new roman", 15, "bold"),bg="#A0D636", fg="white")
      btn_print.place(x=0,y=70, width=148, height=68)
      
      btn_clear_all=Button(billMenuFrame, text= 'Clear',command=self.clear_all,font=("Times new roman", 15, "bold"),bg="#2FA236", fg="white")
      btn_clear_all.place(x=147,y=70, width=148, height=68)
      
      btn_generate=Button(billMenuFrame, text= 'Generate Bill',command=self.generate_bill ,font=("Times new roman", 15, "bold"),bg="#333ED4", fg="white")
      btn_generate.place(x=295,y=70, width=148, height=68) 
      
      self.Show()
      self.update_date_time()
      
    #===Functions===
    def get_input(self,num):
      num=self.var_cal_input. get ()+str (num)
      self.var_cal_input.set (num)
      
    def clear_cal(self):
      self.var_cal_input.set("")
      
    def perform_cal(self):
      result=self.var_cal_input.get ()
      self.var_cal_input.set(eval(result))
        
    def Show(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
        cur.execute("SELECT * FROM product where status = 'Active'")
        rows = cur.fetchall()
        self.Product_Table.delete(*self.Product_Table.get_children())
        if rows:
          for row in rows:
            self.Product_Table.insert("", END, values=row)
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
    def search(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      if not self.variable_search.get()==None:
         messagebox.showerror("Error", "Please enter search criteria", parent=self.root)
         return

      try:
         query = "SELECT * FROM product WHERE name LIKE ? AND status = 'Active'"
         cur.execute(query, ('%' + self.variable_search.get() + '%',))
         rows = cur.fetchall()
         if rows:
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
               self.Product_Table.insert("", END, values=row)
         else:
            messagebox.showerror("Error", "No records found", parent=self.root)
      except Exception as ex:
         messagebox.showerror("Error", "Error due to: " + str(ex), parent=self.root) 
         
    def get_data(self, ev):
      f=self.Product_Table.focus ()
      content=(self.Product_Table.item(f))
      row=content [ 'values' ]
      self.var_pid.set(row[0])
      self.var_name.set(row[2])
      self.var_price.set(row[3])
      self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
      self.var_stock.set(row[4])
      self.var_qty.set("1")
    
    def get_data_cart(self, ev):
      f=self.CartTable.focus ()
      content=(self.CartTable.item(f))
      row=content[ 'values' ]
      self.var_pid.set(row[0])
      self.var_name.set(row[1])
      self.var_price.set(row[2])
      self.var_qty.set(row[3])
      self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
      self.var_stock.set(row[4])
      
    
    def add_update_cart(self):
      if self. var_pid.get()=="":
        messagebox. showerror ('Error', "Select a product from the list" ,parent=self.root)   
      elif self.var_qty.get()=="":
        messagebox. showerror ('Error', "Enter the quantity required" ,parent=self.root)
      elif int(self.var_qty.get()) > int(self.var_stock.get())  :
        messagebox. showerror ('Error', "Invalid Quantity" ,parent=self.root) 
      else:
        
        price_cal=self.var_price.get()
        cart_data=[self.var_pid.get(),self.var_name.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
         
        present="no"
        index_=0
        for row in self.cart_list:
          if self.var_pid.get()==row[0]:
            present="yes"
            break
          index_+=1
        if present == "yes":
             op=messagebox.askyesno("Confirm, do you want to update the current list?",parent=self.root)
             if op == True:
                  if self.var_qty.get() =="0":
                    self.cart_list.pop(index_)
                  else:
                    #self.cart_list[index_][2]=price_cal
                    self.cart_list[index_][3]=self.var_qty.get()
                       
        else:          
          self.cart_list.append(cart_data) 
        self.show_cart()
        self.bill_updates()
        
    def bill_updates (self):
      self.bill_amnt=0
      self.net_pay=0
      self.discount=0
      for row in self.cart_list:
        self.bill_amnt=self.bill_amnt+(float(row[2])* int(row[3]))
      self.discount=(self.bill_amnt*5) /100 
      self.net_pay=self.bill_amnt-self.discount
      self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
      self.lbl_net_pay.config(text=f'Net Pay\n{str (self.net_pay)}')
      self.cartTitle.config(text=f"Cart \t Total Product: [{str(len (self.cart_list))}]") 
        
    def show_cart(self):
      try:
        self.CartTable.delete(*self.CartTable.get_children())
        for row in self.cart_list:
          self.CartTable.insert("", END, values=row)
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
    
    def generate_bill(self):
      if self.var_CustomerName. get ()=='' or self. var_contact.get ()=='':
        messagebox.showerror ("Error", f"Customer Details are required" ,parent=self.root)
      elif len(self.cart_list)==0:
           messagebox.showerror ("Error", f"Please add products to the cart" ,parent=self.root)
           
      else:
      #====BI11 Top====
        self.bill_top()
      #====BI11 Middle==== 
        self.bill_middle() 
      #====BIll Bottom==== 
        self.bill_bottom()
        
        fp=open(f'Bill/{str(self.invoice)}.txt', 'w')
        fp.write(self.txt_bill_area.get('1.0',END))
        fp.close()
        messagebox.showinfo("The invoice has been saved successfully",parent=self.root)
        self.chk_print=1
    
    def bill_top (self):
      self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y") )
      bill_top_temp=f'''
\t\tPocketBiz-Inventory System
\t Phone No. 97152*******, United Arab Emirates
{str ("="*59)}
  Customer Name:{self.var_CustomerName.get()}
  Ph no. :{self.var_contact.get()}
  Bill No. {str(self.invoice)}\t\t\t        Date:{str(time.strftime ("%d/%m/%Y"))}
{str("="*59)}
Product Name\t\t\tQTY            \tPrice
{str ("="*59)} 
      '''
      self.txt_bill_area.delete("1.0",END) 
      self.txt_bill_area.insert("1.0",bill_top_temp)

    def bill_bottom(self):
      bill_bottom_temp =f''' 
{str("="*59)}
Bill Amount\t\t\t\t\t£ {self.bill_amnt}
Discount\t\t\t\t\t£ {self.discount}
Net Pay\t\t\t\t\t£ {self.net_pay}
{str("="*59)}\n
         '''
      self.txt_bill_area.insert(END, bill_bottom_temp) 
      
    def bill_middle(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      try:
        for row in self.cart_list:
          pid=row[0]
          name=row[1]
          qty=int(row[4])-int(row[3])
          if int(row[3]) == int(row[4]):
            status="Inactive"
          if int(row[3]) != int(row[4]):
            status="Active"
          price=float(row[2])*float(row[3])
          price=str(price)
          self.txt_bill_area.insert(END, "\n "+name+"\t\t\t"+row[3]+"\t\t£ "+price)
          cur.execute("Update Product set quantity=?, status=? WHERE pid=? ",( 
             qty,
             status,
             pid                                                                  
          ))
          con.commit()
        con.close() 
        self.Show()
      except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def clear_cart (self):
      self.var_pid.set("")
      self.var_name.set("") 
      self.var_price.set("") 
      self.var_qty.set("")
      self.lbl_inStock.config(text=f"In Stock")
      self.var_stock.set("")  
    
    def clear_all(self):
      del self.cart_list[:] 
      self.var_CustomerName.set(" ")
      self.var_contact.set(" ")
      self.txt_bill_area.delete('1.0' ,END)
      self.cartTitle.config(text=f"Cart \t Total Product:[0]")
      self.variable_search.set(" ")
      self.chk_print=0
      self.clear_cart()
      self.Show()
      self.show_cart()
    
    def update_date_time(self):
      time_=time.strftime ("%H:%M:%S")
      date_=time.strftime ("%d/%m/%Y")
      self.clock.config(text=f"Welcome to PocketBiz\t\t\t Date:{str(date_)}\t\t\t Time:{str(time_)}") 
      self.clock.after(200, self .update_date_time)
    
    def print_bill(self):
      if self.chk_print==1:
        messagebox.showinfo('Print', "Please wait while the bill is printing" ,parent=self.root)
        new_file=tempfile.mktemp(".txt")
        open(new_file, "w").write(self.txt_bill_area.get("1.0" ,END))
        os.startfile(new_file,"print")
      else:
        messagebox.showerror(' Print', "Please generate the bill",parent=self.root)
        
    def Logout (self):
      self.root. destroy ()
      os.system("python3 Login.py")  
           
if __name__ == "__main__":  
   root = Tk()
   billing(root)
   root.mainloop()