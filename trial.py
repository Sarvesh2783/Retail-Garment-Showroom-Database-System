import mysql.connector as co
import tkinter as tk
from tkinter import *
from tkinter import ttk

def display_product_info():
    product_code = product_code_entry.get()
    size = size_entry.get()

    # Connect to MySQL database
    mycon = co.connect(
        host='localhost',
        user='root',
        passwd='Dhairya@29',
        database='Shubham_Collection'
    )
    # Create a cursor object
    cursor = mycon.cursor()

    # Fetch product details from the database based on Product Code and Size
    query = "SELECT Brand, Garment_Type, Quantity, Colour, MRP FROM Product_Details WHERE Product_Code = %s AND Size = %s"
    cursor.execute(query, (product_code, size))
    product_details = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    mycon.close()

    # Display product details in a Tkinter window
    if product_details:
        brand, garment_type, quantity, colour, mrp = product_details

        # Create a new Tkinter window
        info_window = Tk()
        info_window.title("Product Information")
        info_window.geometry("400x200")

        # Create a treeview for displaying product details in a tabular format
        columns = ("Attribute", "Value")
        tree = ttk.Treeview(info_window, columns=columns, show="headings")

        tree.heading("Attribute", text="Attribute")
        tree.heading("Value", text="Value")

        tree.insert("", tk.END, values=("Brand", brand))
        tree.insert("", tk.END, values=("Garment Type", garment_type))
        tree.insert("", tk.END, values=("Quantity", quantity))
        tree.insert("", tk.END, values=("Colour", colour))
        tree.insert("", tk.END, values=("MRP", mrp))

        tree.pack(pady=20)

        # Run the Tkinter event loop
        info_window.mainloop()
    else:
        # Display a message if no product is found
        error_label.config(text="Product not found.")

# Create the main Tkinter window
root = Tk()
root.title("Product Information Fetcher")
root.geometry("400x200")

# Create and set up the GUI components
label1 = Label(root, text="Enter Product Code:")
label1.grid(row=0, column=0, padx=10, pady=10)

product_code_entry = Entry(root)
product_code_entry.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(root, text="Enter Size:")
label2.grid(row=1, column=0, padx=10, pady=10)

size_entry = Entry(root)
size_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = Button(root, text="Fetch Product Info", command=display_product_info)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display error message
error_label = Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
