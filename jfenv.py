import mysql.connector as co
from tkinter import *
import tkinter as tk

def enter_data():
    
    mycon=co.connect(host='localhost',
                        user='root',
                        passwd='Dhairya@29' ,
                        database='Shubham_Collection'
                    )
    
    mycursor = mycon.cursor()

    prod_Brand =str(input("Enter brand: "))
    prod_Garment_Type =str(input("Enter Garment_Type: ") )
    prod_Product_Code =str(input("Enter Product_Code: ") )
    prod_Size =int(input("Enter Size: "))
    prod_Colour =str(input("Enter Colour: ") )
    prod_Quantity =int(input("Enter Quantity: ") )
    prod_MRP =int(input("Enter MRP: ") )

    st = "INSERT INTO Product_Details (Brand, Garment_Type, Product_Code,Size, Colour, Quantity, MRP) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (prod_Brand, prod_Garment_Type, prod_Product_Code, prod_Size, prod_Colour, prod_Quantity, prod_MRP)
    
    # Execute the query
    mycursor.execute(st, val)

    # mycursor.execute(st)
    mycon.commit()
    mycon.close()

# enter_data()