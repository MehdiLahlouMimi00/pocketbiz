import sqlite3
import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Employee import EmployeeClass
from Supplier import SupplierClass
from Category import CategoryClass
from Product import ProductClass
from Sales import SalesClass
from Stock_Analyser import StockAnalyserClass
 
 
class dashboard:
    def __init__(self, root):
      self.root = root
      self.root.title("PocketBiz")
      self.root.geometry("1400x800")
      self.root.config(bg="#CADEED")
      self.root.resizable(False, False)
 
      self.setPosition()
      self.createTitle()
      self.createLogOutButton()
      self.createClock()
 
      
 
      #====Main Buttons====
      
      self.buttons = [
      ('Employees', "#50C878", 100, 150),
      ('Suppliers', "#dcd5b9", 550, 150),
      ('Categories', "#D2042D", 1000, 150),
      ('Products', "#ff4466", 100, 500),
      ('Sales', "#A55D35", 550, 500),
      ('Stock_Analyser', "#FFDB58", 1000,500)
      ]
 
      self.labelButtons()
      
      self.update_date_time()
      
 
    def setPosition(self) : 
           x = (root.winfo_screenwidth() / 2) - (1400 / 2)
           y = (root.winfo_screenheight() / 2) - (800 / 2)                                                 
           self.root.geometry(f"+{int(x)}+{int(y)}")
 
    def createTitle(self) : 
             self.icon_title = Image.open("images/LOGO.png")
             self.icon_title = self.icon_title.resize((50, 50), Image.ANTIALIAS)
             self.icon_title = ImageTk.PhotoImage(self.icon_title)
             self.title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon_title, compound=LEFT, font=("roboto", 40, "bold"), bg="#194569", fg="white", anchor="w", padx=20)
             self.title.place(x=0, y=0, relwidth=1, height=70)
 
    
    def createLogOutButton(self) : 
              Logout_Button = Button(self.root, text="LOGOUT", font=("roboto", 15), cursor="hand2")
              Logout_Button.place(x=1200, y=15, height=50, width=150)
 
 
    def createClock(self) : 
              self.clock = Label(self.root, text="Welcome to PocketBiz\t\t\t Date: DD-MM-YYYY\t\t\t Time: HH:MM:SS ", font=("roboto", 15), bg="#194569", fg="white")
              self.clock.place(x=0, y=70, relwidth=1, height=30)
 
    
 
    def labelButtons(self):
       for button in self.buttons:
        text, color, x, y = button
        command = None
        if text == 'Employees':
            command = self.Employee
        elif text == 'Suppliers':
            command = self.Supplier
        elif text == 'Categories':
            command = self.Category
        elif text == 'Products':
            command = self.Product
        elif text == 'Sales':
            command = self.Sales
        elif text == 'Stock_Analyser':
            command = self.Stock_Analyser
        
            
        button = Button(self.root, text=text, font=("roboto", 20, "bold"), bg=color, fg="black", cursor="hand2", command=command)
        button.place(x=x, y=y, height=150, width=300)

 
    def Employee(self):
      self.new_window = Toplevel(self.root)
      EmployeeClass(self.new_window)
 
    def Supplier(self):
      self.new_window = Toplevel(self.root)
      SupplierClass(self.new_window) 
 
    def Category(self):
      self.new_window = Toplevel(self.root)
      CategoryClass(self.new_window) 
      
    def Product(self):
      self.new_window = Toplevel(self.root)
      ProductClass(self.new_window) 
      
    def Sales(self):
        self.new_window = Toplevel(self.root)
        SalesClass(self.new_window)
    
    def Stock_Analyser(self):
        self.new_window = Toplevel(self.root)
        StockAnalyserClass(self.new_window)
        
    def update_date_time(self):
      time_=time.strftime ("%H:%M:%S")
      date_=time.strftime ("%d/%m/%Y")
      self.clock.config(text=f"Welcome to PocketBiz\t\t\t Date:{str(date_)}\t\t\t Time:{str(time_)}") 
      self.clock.after(200, self .update_date_time)
           
if __name__ == "__main__":
   root = Tk()
   dashboard(root)
   root.mainloop()
