import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt


class StockAnalyserClass : 
    def __init__(self, root) :

        self.root = root
        self.root.title("PocketBiz")
        self.root.geometry("1150x700+275+130")
        self.root.config(bg="#CADEED")
        self.root.focus_force()

        self.bestButton = Button(self.root,text="Highest profit makers", command=self.displayBest)
        self.bestButton.pack()

        self.showProducts()

        self.displayBest()
    
    
    def displayBest(self) : 
        
        try : 
            con = sqlite3.connect(database=r"mydatabase.db")
            cur = con.cursor()

            cur.execute("SELECT name, quantity, price FROM product WHERE STATUS like 'sent' ORDER BY quantity DESC;")
            dump = cur.fetchall()
            quantities = list(map(lambda x:int(x[1]), dump))
            labels = list(map(lambda x:x[0], dump))
            plt.pie(quantities, labels=labels)
            plt.show()

            revenue = list(map(lambda x:int(x[2]), dump))
            plt.pie(revenue, labels=labels)
            plt.show()

        except :
            print("Database issues")

            
    def showProducts(self) :
        
        con = sqlite3.connect(database=r"mydatabase.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM product WHERE STATUS like 'sent'")
        dump = cur.fetchall()

        listbox = Listbox(self.root)
        listbox.pack()

        for i in range(len(dump)) : 
            listbox.insert(END, dump[i][2])    # adding the name
        
        con.close()
        

if __name__ == "__main__":
   root=Tk()
   object=StockAnalyserClass(root)
   root.mainloop()    