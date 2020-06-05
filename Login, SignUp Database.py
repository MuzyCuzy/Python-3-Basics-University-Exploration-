from tkinter import *
import mysql.connector

def check(text):
    child1=Toplevel(root)
    child1.title(text)
    l1=Label(child1,text="User Name : ",width=30)
    l1.grid(row=0,column=0)
    l2=Label(child1,text="Password : ")
    l2.grid(row=1,column=0)
    name=Entry(child1)
    name.grid(row=0,column=1)
    pw=Entry(child1)
    pw.grid(row=1,column=1)
    l3=Label(child1,text="")
    l3.grid(row=2,column=0,columnspan=2)
    if (text=="Login"):
        pw.config(show="*")
        log=Button(child1,text="Next",height=1,width=5,command=lambda:login_func(child1,name,pw,l3))
        log.grid(row=3,column=1)
    elif (text=="Sign Up"):
        sign=Button(child1,text="Next",height=1,width=5,command=lambda:signup_func(child1,name,pw,l3))
        sign.grid(row=3,column=1)

def empty(child1,l3):
    originalbg=child1["bg"]
    l3.config(text="",bg=originalbg)

def login_func(child1,name,pw,l3):
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="login")
    cur=con.cursor()
    flag=False
    cur.execute("select * from password")
    data=cur.fetchall()
    if ((name.get()=="") or (pw.get()=="")):
        l3.config(text="Please enter the required details",bg="red2")
        child1.after(2500,lambda:empty(child1,l3))
        flag=True
    for i in data:
        if ((i[0]==name.get()) and (i[1]==pw.get())):
            messagebox.showinfo("Logged In!","Login Successful")
            flag=True
            break
    if (flag==False):
        messagebox.showerror("Login Failed","Invalid Username Or Password")
    con.close()

def signup_func(child1,name,pw,l3):
    con=mysql.connector.connect(user=input("Enter your MySQL Username :\t"),password=input("Enter your MySQL Password :\t"),database="login")
    cur=con.cursor()
    flag=True
    cur.execute("select * from password")
    data=cur.fetchall()
    n=name.get();p=pw.get()
    if ((n=="") or (p=="")):
        l3.config(text="Please enter the required details",bg="red2")
        child1.after(2500,lambda:empty(child1,l3))
        flag=False
    for i in data:
        if (n==i[0]):
            flag=False
            messagebox.showerror("Invalid Username","Username already in USE")
            break
        elif (p==i[1]):
            flag=False
            messagebox.showerror("Invalid Password","Password already EXISTS")
            break
    if (flag==True):
        cur.execute("insert into password values('"+n+"','"+p+"')")
        con.commit()
        messagebox.showinfo("Sign Up Successful!","You have successfully created your account")
    con.close()
    
root=Tk()
root.title("Sign In/Up")
l=Label(root,text="Do you want to Login or SignUp?",bg="deep sky blue",width=30)
l.grid(row=0,column=0,columnspan=2)
login=Button(root,text="Login",height=1,width=5,command=lambda:check(login["text"]))
login.grid(row=2,column=0)
l_extra=Label(root,text="Welcome!",bg="blue violet",width=30)
l_extra.grid(row=3,column=0,columnspan=2)
signup=Button(root,text="Sign Up",height=1,width=5,command=lambda:check(signup["text"]))
signup.grid(row=2,column=1)
root.mainloop()
