import tkinter as tk
from tkinter import ttk
import mysql.connector as co

def SearchingData():
    mycon = co.connect(
        host='localhost',
        user='root',
        passwd='Dhairya@29',
        database='Shubham_Collection'
    )

    mycursor = mycon.cursor()

    root = tk.Tk()
    root.title("SEARCH PRODUCT")
    root.geometry("1920x1080")

    def search():
        ColumnType = entry1.get()
        query = entry2.get()
        mycursor.execute(f"SELECT * FROM Product_Details WHERE {ColumnType} = '{query}'")
        result = mycursor.fetchall()

        if result:
            error_label.config(text="Product Found", fg='green')
            for i in tree.get_children():
                tree.delete(i)
            for row in result:
                tree.insert("", "end", values=row)
        else:
            error_label.config(text="Product Not Found", fg='red')
            for i in tree.get_children():
                tree.delete(i)

    label1 = tk.Label(root, text="SEARCH DATA", font=('Arial', 35, 'bold'), fg='red')
    label1.pack()

    label2 = tk.Label(root, text="Search By: ", font=('Arial', 18, 'bold'), fg='red')
    label2.place(x=370, y=80)

    s = ttk.Style(root)
    s.theme_use("clam")
    s.configure("Treeview", background="lightblue", foreground='black', fieldbackground='lightblue', rowheight=25)
    s.configure(".", font=('Arial', 10, 'bold'))
    s.configure("Treeview.Heading", font=('Arial', 10, 'bold'), foreground='red', background='#FFFDD0')

    entry1 = ttk.Entry(root, width=30)
    entry1.place(x=500, y=90)
    entry2 = ttk.Entry(root, width=30)
    entry2.place(x=900, y=90)

    error_label = tk.Label(root, text="", font=('Arial', 12), fg='red')
    error_label.pack(pady=10)

    search_button = ttk.Button(root, text="SEARCH PRODUCT", command=search)
    search_button.pack(pady=70)

    tree = ttk.Treeview(root, columns=("Brand", "Garment_Type", "Product_Code", "Size", "Colour", "Quantity", "MRP"), show="headings")
    tree.heading("Brand", text="Brand", anchor=tk.CENTER)
    tree.heading("Garment_Type", text="Garment_Type", anchor=tk.CENTER)
    tree.heading("Product_Code", text="Product_Code", anchor=tk.CENTER)
    tree.heading("Size", text="Size", anchor=tk.CENTER)
    tree.heading("Colour", text="Colour", anchor=tk.CENTER)
    tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
    tree.heading("MRP", text="MRP", anchor=tk.CENTER)
    
    for col in ("Brand", "Garment_Type", "Product_Code", "Size", "Colour", "Quantity", "MRP"):
        tree.column(col, anchor=tk.CENTER)

    tree.pack(expand=True, fill="both")

    root.mainloop()  
