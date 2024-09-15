import mysql.connector as co
from tkinter import *
import tkinter as tk

# Connect to your MySQL database
mycon=co.connect(host='localhost',
                        user='root',
                        passwd='Dhairya@29' ,
                        database='Shubham_Collection'
                    )

# Create a cursor object to execute SQL commands
mycursor = mycon.cursor()

# Create the tkinter application
root = tk.Tk()
root.title("ADD DATA")
root.geometry("1920x1080")
root.config(bg='lightblue')

# photo9=PhotoImage(file='"C:\\Users\\Dhairya Shimpi\\Downloads\\rack-clothes-store_23-2148929537-removebg-preview.png"')

# label15=Label(
#             root,
#             bg="lightblue",
#             image=photo9,
#             compound='top'
#            )
# label15.place(x=250,y=175)

tk.Label(root, text="ENTER PRODUCT DETAILS",font=('Arial',30,'bold'),bg='lightblue',fg='red').pack(side="top")

# Create labels and entry fields for data input
tk.Label(root, text="Brand:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=75)
tk.Label(root, text="Garment Type:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=125)
tk.Label(root, text="Product Code:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=175)
tk.Label(root, text="Size:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=225)
tk.Label(root, text="Colour:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=275)
tk.Label(root, text="Quantity:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=325)
tk.Label(root, text="MRP:",font=('Arial',15,'bold'),bg='lightblue',fg='black').place(x=50,y=375)

Brand_entry = tk.Entry(root)
Garment_Type_entry = tk.Entry(root)
Product_Code_entry = tk.Entry(root)
Size_entry = tk.Entry(root)
Colour_entry = tk.Entry(root)
Quantity_entry = tk.Entry(root)
MRP_entry = tk.Entry(root)

Brand_entry.place(x=200,y=75)
Garment_Type_entry.place(x=200,y=125)
Product_Code_entry.place(x=200,y=175)
Size_entry.place(x=200,y=225)
Colour_entry.place(x=200,y=275)
Quantity_entry.place(x=200,y=325)
MRP_entry.place(x=200,y=375)


# Function to insert data into the MySQL database
def insert_data():
    Brand = Brand_entry.get()
    Garment_Type = Garment_Type_entry.get()
    Product_Code = Product_Code_entry.get()
    Size=Size_entry.get()
    Colour=Colour_entry.get()
    Quantity=Quantity_entry.get()
    MRP=MRP_entry.get()

    sql = "INSERT INTO Product_Details (Brand, Garment_Type, Product_Code, Size, Colour, Quantity, MRP) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Brand, Garment_Type, Product_Code, Size, Colour, Quantity, MRP)
    mycursor.execute(sql, val)
    mycon.commit()

# Create a button to trigger the data insertion
tk.Button(root, text="Add Product", command=insert_data,font=('Arial',25,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=10, height=1).place(x=200,y=425)

root.mainloop()
