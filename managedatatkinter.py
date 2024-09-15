import mysql.connector as co
from tkinter import *
import tkinter as tk
from DataEntry import enter_data

def ManageData():
    newwindow=Tk()
    newwindow.geometry('1920x1080')
    newwindow.title("MANAGE DATA")
    newwindow.config(bg="lightblue")  
    def buttonFunction1():
        print("ADD DATA")
    def buttonFunction2():
        print("SEARCH DATA")    
    def buttonFunction3():
        print("DELETE DATA")
    def buttonFunction4():
        print("SHOW DATA")
    def buttonFunction5():
        print("UPDATE DATA")
    
    photo3=PhotoImage(file='C:\\Users\\Dhairya Shimpi\\Downloads\\tailor-working-client-costume-atelier-shop_276875-16-removebg-preview.png')
    photo4=PhotoImage(file='C:\\Users\\Dhairya Shimpi\\Desktop\\Posters\\ShubhamLogo1.png')
    
    label5=Label(
                newwindow,
                bg="lightblue",
                image=photo3,
                compound='top'
               )
    label5.place(x=800,y=200)
    
    label6=Label(
                newwindow,
                bg="lightblue",
                image=photo4,
                compound='top'
               )
    label5.pack(side=RIGHT)
    
    b1=Button(newwindow,text="ADD DATA",command=enter_data,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b1.place(x=200,y=150)
    b2=Button(newwindow,text="SHOW DATA",command=buttonFunction1,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b2.place(x=200,y=300)
    b3=Button(newwindow,text="SEARCH DATA",command=buttonFunction1,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b3.place(x=200,y=450)
    b4=Button(newwindow,text="DELETE DATA",command=buttonFunction1,font=('Arial',35,'bold'),bg='#FFFDD0',fg='red',borderwidth=3,width=15, height=1)
    b4.place(x=200,y=600)
    
    # newwindow.mainloop()