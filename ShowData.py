import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector as co


def Showdata():
    mycon=co.connect(host='localhost', 
                            user='root',
                            passwd='Sarvesh@27' ,
                            database='Shubham_Collection'
                        )
    
    mycursor = mycon.cursor()
    
    # Fetch data from the MySQL table
    mycursor.execute("SELECT * FROM Product_Details")
    rows = mycursor.fetchall()
    
    root = tk.Tk()
    root.title("SHOW DATA")
    root.geometry("1920x1080")
    
    label1=Label(root,text="SHOW DATA",
                font=('Arial',35,'bold'),
                fg='red'
               )
    label1.pack()
    
    # Creating a treeview
    tree = ttk.Treeview(root)
    tree['show']='headings'    #Using this command the first column is not displayed as empty
    s=ttk.Style(root)
    s.theme_use("clam")
    s.configure("Treeview",
                background="lightblue",
                foreground='black',
                fieldbackground='lightblue',
                rowheight=25
                )

    s.configure(".",font=('Arial',10,'bold'))
    s.configure("Treeview.Heading",font=('Arial',10,'bold'),foreground='red',background='#FFFDD0')
    
    tree["columns"] = tuple([i[0] for i in mycursor.description])

    for col in tree["columns"]:
        tree.column(col, anchor="center",minwidth=50)
        tree.heading(col, text=col)

    for row in rows:
        tree.insert("", "end", values=row)
    
    tree.pack(expand=True,fill="both")
    
    root.mainloop()
