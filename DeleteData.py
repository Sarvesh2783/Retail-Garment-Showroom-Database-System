import tkinter as tk
import mysql.connector as co
from tkinter import *

def DeleteProduct():
    mycon = co.connect(
        host='localhost',
        user='root',
        passwd='Sarvesh@27',
        database='Shubham_Collection'
    )

    mycursor = mycon.cursor()
    
    error_label = None

    def DeletingData():
        product_code = entry_product_code.get()
        size = entry_size.get()
        qty=entry_qty.get()
        # Check if the product exists with the given code and size
        select_query = "SELECT Quantity FROM Product_Details WHERE Product_Code = %s AND Size = %s;"
        mycursor.execute(select_query, (product_code, size))
        result = mycursor.fetchone()

        if result:
            # If quantity is greater than 0, update the quantity
            if result[0] > 0:
                update_query = "UPDATE Product_Details SET Quantity = Quantity - %s WHERE Product_Code = %s AND Size = %s;"
                mycursor.execute(update_query, (qty,product_code, size))
                mycon.commit()
                print(mycursor.rowcount)

                error_label.config(text="Data Deleted Successfully", fg='red')
            else:
                error_label.config(text="Quantity is already 0 for the specified product and size", fg='red')
        else:
            error_label.config(text="Product not found for the specified code and size", fg='red')

    root = tk.Tk()
    root.title("DELETE DATA")
    root.geometry("1920x1080")
    root.config(bg='lightblue')
    
    label_product_code = tk.Label(root, text="Enter Product Code: ", font=("Arial", 20, "bold"), fg='red', bg='lightblue')
    label_product_code.place(x=640, y=40)

    entry_product_code = tk.Entry(root)
    entry_product_code.place(x=705, y=90)

    label_size = tk.Label(root, text="Enter Size: ", font=("Arial", 20, "bold"), fg='red', bg='lightblue')
    label_size.place(x=690, y=150)

    entry_size = tk.Entry(root)
    entry_size.place(x=705, y=200)

    label_qty = tk.Label(root, text="Enter Quantity to be deleted: ", font=("Arial", 20, "bold"), fg='red', bg='lightblue')
    label_qty.place(x=600, y=250)

    entry_qty = tk.Entry(root)
    entry_qty.place(x=705, y=300)

    button = tk.Button(root, text="Delete", command=DeletingData,font=('Arial',15),borderwidth=3,width=15, height=1)
    button.place(x=680, y=380)

    error_label = tk.Label(root, text="", font=("Arial", 14), fg='red', bg='lightblue')
    error_label.place(x=640, y=350)

    root.mainloop()
