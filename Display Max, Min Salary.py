from tkinter import *
import mysql.connector

def max_sal():
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="employee")
    cur=con.cursor()
    cur.execute("select * from emp")
    data=cur.fetchall()
    maxsal=0
    for i in data:
        if (i[2]>maxsal):
            maxsal=i[2]
    maxl.config(text=str(maxsal))

def min_sal():
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="employee")
    cur=con.cursor()
    cur.execute("select * from emp")
    data1=cur.fetchone()
    minsal=data1[2]
    data2=cur.fetchall()
    for i in data2:
        if (i[2]<minsal):
            minsal=i[2]
    minl.config(text=str(minsal))

def search_record():
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="employee")
    cur=con.cursor()
    en=e.get()
    record=""
    if (en=="" or en.isdigit()):
        lsearch.config(text="Please enter the correct name",bg="red2")
        lsearch.after(2000,entry_error)
    else:
        cur.execute("select * from emp")
        data=cur.fetchall()
        for i in data:
            if (i[1]==en):
                record=i
                break
        if (record==""):
            lsearch.config(text="No record with matching name found",bg="red2")
            lsearch.after(2000,entry_error)
        else:
            lsearch.config(text="ID : "+str(record[0])+"\tName : "+str(record[1])+"\tSalary : "+str(record[2]),bg="deep sky blue")

def entry_error():
    originalbg=root["bg"]
    lsearch.config(text="",bg=originalbg)

root=Tk()
root.title("Details")
bsearch=Button(root,text="Search",width=11,command=search_record)
bsearch.grid(row=0,column=0)
e=Entry(root)
e.grid(row=0,column=1)
lsearch=Label(root,text="")
lsearch.grid(row=1,column=0,columnspan=2)
bmax=Button(root,text="Maximum Salary",command=max_sal)
bmax.grid(row=4,column=0)
maxl=Label(root,text="")
maxl.grid(row=4,column=1)
bmin=Button(root,text="Minimum Salary",command=min_sal)
bmin.grid(row=5,column=0)
minl=Label(root,text="")
minl.grid(row=5,column=1)
