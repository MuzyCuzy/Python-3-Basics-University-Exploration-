from tkinter import *
count=0
no=[];char=[]
ans=0;flag=False

def num(text):
    global count;global no;
    if (count==0):
        clr()
    e.insert(count,text)
    count+=1

def operation(text):
    global count;global char
    clr()
    count=0
    e.insert(count,0)
    char.append(text)

def check(text):
    global no;global flag;global char;global ans
    en=e.get()
    try:
        no.append(int(en))
    except ValueError:
        pass
    if (text=="+" or text=="-" or text=="*" or text=="/"):
        operation(text)
    if ((len(char)==2) and (text=="+" or text=="-" or text=="*" or text=="/")):
        equal(text,flag=True)
    elif (len(char)==1 and text=="="):
        equal(text,flag=True)
    else:
        equal(text,flag=False)

def equal(text,flag):
    global ans;global char;global no;global count;
    clr()
    try:
        if (text=="+" or text=="-" or text=="*" or text=="/"):
                if (flag==True):
                    if (char[0]=="+"):
                        ans=no[0]+no[1]
                    elif (char[0]=="-"):
                        ans=no[0]-no[1]
                    elif (char[0]=="*"):
                        ans=no[0]*no[1]
                    else:
                        ans=no[0]/no[1]
                    flag=False
                else:
                    if (char[len(char)-2]=="+"):
                        ans+=no[len(no)-1]
                    elif (char[len(char)-2]=="-"):
                        ans-=no[len(no)-1]
                    elif (char[len(char)-2]=="*"):
                        ans*=no[len(no)-1]
                    elif (char[len(char)-2]=="/"):
                        ans/=no[len(no)-1]
                e.insert(count,str(ans))
        elif (text=="="):
            if (flag==True):
                if (char[0]=="+"):
                        ans=no[0]+no[1]
                elif (char[0]=="-"):
                        ans=no[0]-no[1]
                elif (char[0]=="*"):
                        ans=no[0]*no[1]
                else:
                        ans=no[0]/no[1]
                flag=False
                e.insert(count,str(ans))
            else:
                if (char[len(char)-1]=="+"):
                        ans+=no[len(no)-1]
                elif (char[len(char)-1]=="-"):
                        ans-=no[len(no)-1]
                elif (char[len(char)-1]=="*"):
                        ans*=no[len(no)-1]
                elif (char[len(char)-1]=="/"):
                        ans/=no[len(no)-1]
                e.insert(count,str(ans))
                ans=0;count=0;no=[];char=[]
    except IndexError:
        pass
    
def clr():
    e.delete(0,END)

def cleanse():
    global count;global ans;global char;global no
    clr()
    ans=0;count=0;no=[];char=[]
    
root=Tk()
root.title("Calculator")
root.configure(background="thistle2")
e=Entry(root,bd=5,width=28)
e.grid(row=0,column=0,columnspan=8)
b1=Button(root,text="1",bd=5,height=1,width=5,command=lambda:num(b1["text"]))
b1.grid(row=1,column=0)
b2=Button(root,text="2",bd=5,height=1,width=5,command=lambda:num(b2["text"]))
b2.grid(row=1,column=1)
b3=Button(root,text="3",bd=5,height=1,width=5,command=lambda:num(b3["text"]))
b3.grid(row=1,column=2)
ba=Button(root,text="+",bd=5,height=1,width=5,command=lambda:check(ba["text"]))
ba.grid(row=1,column=3)
b4=Button(root,text="4",bd=5,height=1,width=5,command=lambda:num(b4["text"]))
b4.grid(row=2,column=0)
b5=Button(root,text="5",bd=5,height=1,width=5,command=lambda:num(b5["text"]))
b5.grid(row=2,column=1)
b6=Button(root,text="6",bd=5,height=1,width=5,command=lambda:num(b6["text"]))
b6.grid(row=2,column=2)
bs=Button(root,text="-",bd=5,height=1,width=5,command=lambda:check(bs["text"]))
bs.grid(row=2,column=3)
b7=Button(root,text="7",bd=5,height=1,width=5,command=lambda:num(b7["text"]))
b7.grid(row=3,column=0)
b8=Button(root,text="8",bd=5,height=1,width=5,command=lambda:num(b8["text"]))
b8.grid(row=3,column=1)
b9=Button(root,text="9",bd=5,height=1,width=5,command=lambda:num(b9["text"]))
b9.grid(row=3,column=2)
bm=Button(root,text="*",bd=5,height=1,width=5,command=lambda:check(bm["text"]))
bm.grid(row=3,column=3)
b0=Button(root,text="0",bd=5,height=1,width=5,command=lambda:num(b0["text"]))
b0.grid(row=4,column=0)
bc=Button(root,text="Clear",bd=5,height=1,width=5,command=cleanse,bg="blue violet",fg="deep sky blue",activebackground="midnight blue",activeforeground="thistle2",font=("Impact",13))
bc.grid(row=4,column=1)
be=Button(root,text="=",bd=5,height=1,width=5,command=lambda:check(be["text"]),bg="black",fg="cyan",activebackground="purple4",activeforeground="lavender",font=("Impact",13))
be.grid(row=4,column=2)
bd=Button(root,text="/",bd=5,height=1,width=5,command=lambda:check(bd["text"]))
bd.grid(row=4,column=3)
widget_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b0]
widget_operation=[ba,bs,bm,bd]
for i in widget_list:
    i.configure(bg="MediumPurple1",fg="midnight blue",activebackground="midnight blue",activeforeground="lavender",font=("Impact",13))
for i in widget_operation:
    i.configure(bg="deep sky blue",fg="midnight blue",activebackground="black",activeforeground="cyan",font=("Impact",13))

