import mysql.connector as co
from tkinter import *
import tkinter as tk
# from managedatatkinter import ManageData
from DataEntry import enter_data
from ShowData import Showdata
from SearchData import SearchingData
from DeleteData import DeleteProduct
from Billing import Bill1

window=Tk()
window.title("SHUBHAM COLLECTION")
window.geometry('1920x1080')

window.config(bg="lightblue")    

photo3=PhotoImage(file='C:\\Users\\Dhairya Shimpi\\Desktop\\PYTHON PROJECT\\managedata.png')
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Manage data
def ManageData():
    newwindow=Toplevel(window)
    newwindow.title("MANAGE DATA")
    newwindow.geometry('1920x1080')
    newwindow.config(bg="lightblue")  
    
    label10=Label(
                newwindow,
                bg="lightblue",
                image=photo3,
                compound='top'
               )
    label10.place(x=800,y=200)
    
    b1=Button(newwindow,text="ADD DATA",command=enter_data,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b1.place(x=200,y=150)
    b2=Button(newwindow,text="SHOW DATA",command=Showdata,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b2.place(x=200,y=300)
    b3=Button(newwindow,text="SEARCH DATA",command=SearchingData,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b3.place(x=200,y=450)
    b4=Button(newwindow,text="DELETE DATA",command=DeleteProduct,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b4.place(x=200,y=600)
    
    # newwindow.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------

b1=Button(window,text="Manage Stock",command=ManageData,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
b1.place(x=200,y=350)

b2=Button(window,text="Print Bill",command=Bill1,font=('Arial',35,'bold'),fg='red',bg='#FFFDD0',borderwidth=3,width=15, height=1)
b2.place(x=200,y=500)

photo=PhotoImage(file='C:\\Users\\Dhairya Shimpi\\Desktop\\Posters\\ShubhamLogo1.png')
photo2=PhotoImage(file='C:\\Users\\Dhairya Shimpi\\Downloads\\123.png')

label1=Label(window,text="SHUBHAM COLLECTION",
            font=('Arial',50,'bold'),
            fg='red',
            bg="lightblue",
            image=photo,
            compound='top'
           )
label1.pack()


label3=Label(window,text="Your Fashion",
            font=('Arial',25,'bold'),
            fg='red',
            bg="lightblue"
           )
label3.place(x=660,y=750)

label2=Label(window,text="Our Passion",
            font=('Arial',25,'bold'),
            fg='red',
            bg="lightblue"
           )
label2.place(x=670,y=790)

label4=Label(
            window,
            bg="lightblue",
            image=photo2,
            compound='top'
           )
label4.place(x=800,y=250)

window.mainloop()