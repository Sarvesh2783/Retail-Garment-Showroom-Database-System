import mysql.connector

import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to your MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="garment_shop"
)
cursor = db.cursor()

# Create a table (if it doesn't exist already)
cursor.execute("CREATE TABLE IF NOT EXISTS garments (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), quantity INT, price INT)")

# Define functions for interacting with the database
def insert():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    sql = "INSERT INTO garments (name, quantity, price) VALUES (%s, %s, %s)"
    val = (name, quantity, price)
    cursor.execute(sql, val)
    db.commit()
    messagebox.showinfo("Success", "Record inserted successfully.")

# Create the GUI
root = Tk()
root.title("Garment Shop Database")

name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

quantity_label = Label(root, text="Quantity")
quantity_label.grid(row=1, column=0)
quantity_entry = Entry(root)
quantity_entry.grid(row=1, column=1)

price_label = Label(root, text="Price")
price_label.grid(row=2, column=0)
price_entry = Entry(root)
price_entry.grid(row=2, column=1)

submit_button = Button(root, text="Submit", command=insert)
submit_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
