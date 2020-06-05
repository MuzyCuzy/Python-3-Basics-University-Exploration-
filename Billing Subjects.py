from tkinter import *

def subject(var,txt):
    t.delete(1.0,END)
    total=0
    price=[100,200,300,400,500,600,700] #assume python's price 100,c programming's price 200 and so on
    t.insert(INSERT,"You selected following Subjects:\n")
    for i in range(0,7):
        if (var[i].get()==1):
            total+=price[i]
            t.insert(INSERT,"*"+txt[i]+"\n")
    if (total!=0):
        t.insert(INSERT,"Total Amount : "+str(total))
    else:
        t.insert(INSERT,"No Subjects Selected")
    
root=Tk()
root.title("Subjects")
l=Label(root,text="Select Your Subjects")
l.grid(row=0,column=0)
a=IntVar();b=IntVar();c=IntVar();d=IntVar();e=IntVar();f=IntVar();g=IntVar();
var=[a,b,c,d,e,f,g]
cb=["python","cpro","linux","ds","stats","cal","greenit"]
txt=["Python 2","C Programming","Linux","Data Structures","Statistics","Calculus","Green I.T."]
for i in range(0,7):
    cb[i]=Checkbutton(root,text=txt[i],variable=var[i],width=35,anchor=W)
    (cb[i]).grid(row=i+1,column=0)
b=Button(root,text="Total",width=5,command=lambda:subject(var,txt))
b.grid(row=8,column=0)
t=Text(root,height=9,width=35)
t.grid(row=9,column=0)


