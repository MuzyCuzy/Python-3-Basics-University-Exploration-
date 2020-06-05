from tkinter import *
import mysql.connector

def desp():
    t.delete(1.0,END)
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="employee")
    cur=con.cursor()
    cur.execute("select * from emp")
    data=cur.fetchall()
    for i in data:
        for j in i:
            t.insert(INSERT,str(j))
            t.insert(INSERT,"\t\t")
        t.insert(INSERT,"\n")
            
    
root=Tk()
displayall=Button(root,text="Display All",command=desp)
displayall.pack()
t=Text(root)
t.pack()
