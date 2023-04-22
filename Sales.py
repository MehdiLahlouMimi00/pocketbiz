import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import os


class SalesClass:
      def __init__(self, root):
        self.root = root
        self.root.title("PocketBiz")
        self.root.geometry("1150x700+275+130")
        self.root.config(bg="#CADEED")
        self.root.focus_force()
        self.Bill_List = []
        self.Invoice = StringVar()

        self.createTitle()


        # ====Title====
      def createTitle(self) : 
        Title = Label(self.root, text="Bill Viewer", font=("Roboto", 30),bg="#194569", fg="#FFFFFF", bd=2, relief=RIDGE)
        Title.pack(side=TOP, fill=X, pady=2)
        Invoice = Label(self.root, text="Invoice.No", font=("Roboto", 20), bg="#CADEED")
        Invoice.place(x=50, y=70)
        invoice_txt = Entry(self.root, textvariable=self.Invoice, font=("Roboto", 20), bg="#FFFFFF")
        invoice_txt.place(x=160, y=70, width=180, height=30)
        Search_btn = Button(self.root, text="Search", command=self.search, font=("Roboto", 20),
                             bg="#2196f3", bd=2, relief=RIDGE, cursor="hand2")
        Search_btn.place(x=360, y=70, width=120, height=30)
        Clear_btn = Button(self.root, text="Clear", command=self.clear, font=("Roboto", 20), bg="#2196f3",
                            bd=2, relief=RIDGE, cursor="hand2")
        Clear_btn.place(x=480, y=70, width=120, height=30)

        Sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        Sales_Frame.place(x=0, y=140, width=1150, height=250)
        Scrolly = Scrollbar(Sales_Frame, orient=VERTICAL)
        Scrolly.pack(side=RIGHT, fill=Y)
        self.Sales_List = Listbox(Sales_Frame, font=("Roboto", 20), bg="#FFFFFF", yscrollcommand=Scrolly.set)
        Scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)
        self.Sales_List.bind('<ButtonRelease-1>', self.get_data)

        Bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        Bill_Frame.place(x=0, y=380, width=1150, height=300)
        Bill_Frame_Title = Label(Bill_Frame, text="Customer Bill", font=("Roboto", 15), bg="#194569", fg="#FFFFFF")
        Bill_Frame_Title.pack(side=TOP, fill=X)
        Scrolly2 = Scrollbar(Bill_Frame, orient=VERTICAL)
        Scrolly2.pack(side=RIGHT, fill=Y)
        self.Bill_List = Listbox(Bill_Frame, font=("Roboto", 20), yscrollcommand=Scrolly2.set)
        Scrolly2.config(command=self.Bill_List.yview)
        self.Bill_List.pack(fill=BOTH, expand=1)
        self.show()

      def show(self):
         self.Bill_List.delete(0, END)
         self.Sales_List.delete(0, END)
         if os.path.isdir("bill"):
            for i in os.listdir("bill"):
               if i.split(".")[1] == "txt":
                  self.Sales_List.insert(END, i)
                  
         else:
            messagebox.showinfo("No Data", "No bill data available.", parent=self.root)


      def get_data(self, ev):
         index = self.Sales_List.curselection()
         file_name = self.Sales_List.get(index)
         print(file_name)
         self.Bill_List.delete(0, END)
         with open(f'bill/{file_name}', 'r') as fp:
            for i in fp:
               self.Bill_List.insert(END, i)

      def search(self):
         if self.Invoice.get() == "":
            messagebox.showerror("Error", "Please Enter Invoice No.", parent=self.root)
         else:
            invoice_no = self.Invoice.get()
            found = False
            for file_name in os.listdir("bill"):
               if file_name.endswith(".txt") and file_name.startswith(invoice_no):
                  self.Bill_List.delete(0, END)
                  with open(os.path.join("bill", file_name), 'r') as fp:
                     for i in fp:
                        self.Bill_List.insert(END, i)
                  found = True
                  break
            if not found:
               messagebox.showerror("Error", "Invoice not found.", parent=self.root)


      def clear(self):
         self.Invoice.set("")
         self.Bill_List.delete(0, END)

               
if __name__ == "__main__":
   root=Tk()
   object=SalesClass(root)
   root.mainloop()