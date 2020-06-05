from tkinter import *

def flavour():
    if (check.get()==1):
        messagebox.showinfo("Price","ButterScotch : 40 Per Kg")
    elif (check.get()==2):
        messagebox.showinfo("Price","Chocolate Chip : 20 Per Kg")
    elif (check.get()==3):
        messagebox.showinfo("Price","Cotton Candy : 80 Per Kg")
    else:
        messagebox.showwarning("Warning!","No Flavour Selected")
    
root=Tk()
root.title("Ice-Creams...")
root.config(bg="misty rose")
check=IntVar()
l=Label(root,bg="lavender",text="Select Your Flavour",width=35)
l.pack()
bs=Radiobutton(root,text="ButterScotch",variable=check,value=1,bg="moccasin",fg="chocolate",activebackground="misty rose")
bs.pack()
ch=Radiobutton(root,text="Chocolate Chip",variable=check,value=2,bg="peru",fg="brown4",activebackground="misty rose")
ch.pack()
cc=Radiobutton(root,text="Cotton Candy",variable=check,value=3,bg="orchid1",fg="DodgerBlue4",activebackground="misty rose")
cc.pack()
b=Button(root,text="OK!",command=flavour,height=1,width=5,bg="lavender")
b.pack(fill=BOTH,side=BOTTOM)#fill is taken in x and y
