import mysql.connector
from tkinter import *

def addemp():
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="employee")
    cur=con.cursor()
    idn=e1.get();name=e2.get();sal=e3.get()
    if (idn.isdigit() and sal.isdigit()):
        cur.execute("insert into emp values('"+idn+"','"+name+"','"+sal+"')")
        con.commit()
        con.close()
        l4.config(text="Employee successfully added",bg="deep sky blue")
    else:
        l4.configure(text="ID and Salary should be in DIGITS",bg="orange red")
    root.after(4000,lab)

def lab():
    originalbg=root["bg"]
    l4.configure(text="",bg=originalbg)

root=Tk()
root.title("Add Employee")
l1=Label(root,text="I.D.",width=30)
l1.grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
l2=Label(root,text="Name")
l2.grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)
l3=Label(root,text="Salary")
l3.grid(row=2,column=0)
e3=Entry(root)
e3.grid(row=2,column=1)
addemp=Button(root,text="Add Employee",command=addemp)
addemp.grid(row=4,column=0)
l4=Label(root,text="",width=30)
l4.grid(row=3,column=0)
root.mainloop()
