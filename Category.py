import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class CategoryClass:
   def __init__(self, root):
      self.root = root
      self.root.title("PocketBiz")
      self.root.geometry("1150x700+275+130")
      self.root.config(bg="#CADEED")
      self.root.focus_force()
        
      #====Variables====
      self.category_id = StringVar()
      self.category_name = StringVar()

      self.createTable()
      self.createTitle()
      
        
      #====Title====
   def createTitle(self) : 
         Title=Label(self.root, text="Product Category Manager", font=("Roboto", 30),bg="#194569",fg="#FFFFFF", bd= 2 , relief=RIDGE).pack(side=TOP, fill=X, pady=2)
         Name=Label(self.root, text="Enter Category Name", font=("Roboto", 30 ),bg="#CADEED").place(x=50, y=100)
         self.Name_Entry = Entry(self.root, font=("Roboto", 20), bg="#FFFFFF")
         self.Name_Entry.place(x=350, y=104, width=300)
         
         Save=Button(self.root, text="Save", command=self.save, font=("Roboto", 18), bg="#194569")
         Save.place(x=660, y=104, width=100, height=35)
         Delete=Button(self.root, text="Delete", command=self.delete_category, font=("Roboto", 18), bg="#194569")
         Delete.place(x=760, y=104, width=100, height=35)
        
      #====Table====
   def createTable(self) : 
         table = Frame(self.root, bd=3, relief=RIDGE) 
         table.place(x=0, y=220, height=475, width=1148)
         vertical_scroll = Scrollbar(table, orient=VERTICAL)
         horizontal_scroll = Scrollbar(table, orient=HORIZONTAL)
         self.table = ttk.Treeview(table, columns=("cid", "name"), yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)
         
         headings = [
            ("cid", "Category ID"),
            ("name", "Name"),
         ]
         
         for heading in headings:
            self.table.heading(heading[0], text=heading[1])
         
            self.table["show"] = "headings"
            self.table.column("cid", width=100)
            self.table.column("name", width=100)
            self.table.pack(fill=BOTH, expand=1)
            #self.table.bind("<ButtonRelease - 1 >", self.table_click)
         
            vertical_scroll.pack(side=BOTTOM, fill=X)
            horizontal_scroll.pack(side=RIGHT, fill=Y)
            vertical_scroll.config(command=self.table.yview)
            horizontal_scroll.config(command=self.table.xview)
         
            self.show()
    
   def save(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      name = self.Name_Entry.get()

      if not name:
         messagebox.showerror("Error", "Please enter the Category name", parent=self.root)
         return

      cur.execute("SELECT * FROM category WHERE name=?", (name,))
      row = cur.fetchone()

      if row:
         messagebox.showerror("Error", f"Category with name {name} already exists", parent=self.root)
      else:
         cur.execute("""
               INSERT INTO category (name)
               VALUES (?)
            """, (name,))
         con.commit()
         messagebox.showinfo("Success", f"Category with name {name} saved successfully", parent=self.root)
         self.show()

      con.close()
        
   def show(self):
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      cur.execute("SELECT * FROM category")
      rows = cur.fetchall()
      
      if len(rows)!=0:
         self.table.delete(*self.table.get_children())
         for row in rows:
            self.table.insert('', END, values=row)
         con.commit()
      con.close()

   def delete_category(self):
      # Get the currently selected category
      selected_item = self.table.selection()
      if not selected_item:
         messagebox.showerror("Error", "Please select a category to delete", parent=self.root)
         return

      # Get the ID of the selected category
      category_id = self.table.item(selected_item)['values'][0]

      # Delete the category from the database
      con = sqlite3.connect(database=r"employee.db")
      cur = con.cursor()
      cur.execute("DELETE FROM category WHERE cid=?", (category_id,))
      con.commit()
      con.close()

      # Delete the selected category from the treeview
      self.table.delete(selected_item)

      messagebox.showinfo("Success", "Category deleted successfully", parent=self.root)
         
if __name__ == "__main__":
   root=Tk()
   object=CategoryClass(root)
   root.mainloop()    
