import tkinter as tk
from tkinter import ttk
import mysql.connector as co
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Bill1():
    mycon = co.connect(
        host='localhost',
        user='root',
        passwd='Dhairya@29',
        database='Shubham_Collection'
    )

    mycursor = mycon.cursor()

    root = tk.Tk()
    root.title("BILL")
    root.geometry("1920x1080")

    product_list = []

    def bill():
        Product_Code = entry1.get()
        Size = entry2.get()
        Qty = entry3.get()

        query = "SELECT Brand, Garment_Type, Product_Code, Size, Colour, MRP FROM Product_Details WHERE Product_Code=%s AND Size=%s"
        mycursor.execute(query, (Product_Code, Size))
        result = mycursor.fetchall()

        for row in result:
            row_with_qty = row + (Qty,)
            product_list.append(row_with_qty)
            tree.insert("", "end", values=row_with_qty)

        # Clear the entry fields
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)

    def send_final_bill():
        total_amount = sum(float(row[-2]) * float(row[-1]) for row in product_list)
        discount_percentage = entry_discount.get()

        # Check if a discount percentage is provided
        if discount_percentage:
            discount_amount = (float(discount_percentage) / 100) * total_amount
            discounted_total = total_amount - discount_amount
            total_label.config(text=f"Total Amount: {total_amount:.2f} \n Discounted Amount: {discounted_total:.2f}")
        else:
            total_label.config(text=f"Total Amount: {total_amount:.2f}")

        # Get the customer's email
        customer_email = entry_email.get()

        # Send the final bill via email
        send_bill_via_email(customer_email, product_list, total_amount, discount_percentage)

        # Update the product quantity in the database
        for row in product_list:
            update_query = "UPDATE Product_Details SET Quantity = Quantity - %s WHERE Product_Code = %s AND Size = %s;"
            mycursor.execute(update_query, (row[-1], row[2], row[3]))
            mycon.commit()

        # Clear the product list
        product_list.clear()

    label1 = tk.Label(root, text="BILLING", font=('Arial', 35, 'bold'), fg='red')
    label1.pack()

    label2 = tk.Label(root, text="Product_Code: ", font=('Arial', 15, 'bold'), fg='red')
    label2.place(x=200, y=85)
    label3 = tk.Label(root, text="Size: ", font=('Arial', 15, 'bold'), fg='red')
    label3.place(x=650, y=85)
    label4 = tk.Label(root, text="Quantity: ", font=('Arial', 15, 'bold'), fg='red')
    label4.place(x=1000, y=85)

    label_discount = tk.Label(root, text="Discount (%): ", font=('Arial', 15, 'bold'), fg='red')
    label_discount.place(x=50, y=670)

    label_email = tk.Label(root, text="Email: ", font=('Arial', 15, 'bold'), fg='red')
    label_email.place(x=50, y=710)

    entry1 = ttk.Entry(root, width=30)
    entry1.place(x=350, y=90)
    entry2 = ttk.Entry(root, width=30)
    entry2.place(x=710, y=90)
    entry3 = ttk.Entry(root, width=30)
    entry3.place(x=1100, y=90)

    entry_discount = ttk.Entry(root, width=10)
    entry_discount.place(x=200, y=675)

    entry_email = ttk.Entry(root, width=30)
    entry_email.place(x=200, y=715)

    add_to_bill_button = ttk.Button(root, text="ADD TO BILL", command=bill)
    add_to_bill_button.place(x=730,y=135)

    send_final_bill_button = ttk.Button(root, text="SEND FINAL BILL", command=send_final_bill)
    send_final_bill_button.place(x=715,y=180)

    s = ttk.Style(root)
    s.theme_use("clam")
    s.configure("Treeview", background="lightblue", foreground='black', fieldbackground='lightblue', rowheight=25)
    s.configure(".", font=('Arial', 10, 'bold'))
    s.configure("Treeview.Heading", font=('Arial', 10, 'bold'), foreground='red', background='#FFFDD0')

    tree = ttk.Treeview(root, columns=("Brand", "Garment_Type", "Product_Code", "Size", "Colour", "MRP", "Quantity"), show="headings")
    tree.heading("Brand", text="Brand", anchor=tk.CENTER)
    tree.heading("Garment_Type", text="Garment_Type", anchor=tk.CENTER)
    tree.heading("Product_Code", text="Product_Code", anchor=tk.CENTER)
    tree.heading("Size", text="Size", anchor=tk.CENTER)
    tree.heading("Colour", text="Colour", anchor=tk.CENTER)
    tree.heading("MRP", text="MRP", anchor=tk.CENTER)
    tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)

    for col in ("Brand", "Garment_Type", "Product_Code", "Size", "Colour", "Quantity", "MRP"):
        tree.column(col, anchor=tk.CENTER)

    tree.place(x=15, y=250, width=1500, height=400)

    total_frame = tk.Frame(root, bd=5, relief=tk.GROOVE, bg="lightgrey")
    total_frame.place(x=1100, y=670, width=290, height=120)

    total_label = tk.Label(total_frame, text="", font=('Arial', 15, 'bold'), fg='blue', bg="lightgrey")
    total_label.pack(fill=tk.BOTH)

    root.mainloop()

def send_bill_via_email(customer_email, product_list, total_amount, discount_percentage):
    # Your email credentials
    email_address = 'dhairyashimpi2907@gmail.com'
    email_password = 'dlck vndy kczo dkes'

    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = customer_email
    msg['Subject'] = 'Your Purchase Bill'

    # Create the body of the email
    bill_text = "BILL DETAILS:\n"
    for row in product_list:
        bill_text += f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - Quantity: {row[6]}\n"

    bill_text += f"\nTotal Amount: {total_amount:.2f}"

    # Check if a discount percentage is provided
    if discount_percentage:
        discount_amount = (float(discount_percentage) / 100) * total_amount
        discounted_total = total_amount - discount_amount
        bill_text += f"\nDiscounted Amount: {discounted_total:.2f}"

    msg.attach(MIMEText(bill_text, 'plain'))

    # Set up the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, customer_email, msg.as_string())

    print(f"Bill sent to {customer_email} via email.")    
    