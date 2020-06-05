from tkinter import *
root=Tk()
c=Canvas(root,height=500,width=500)
c.pack()
c.create_rectangle(0,0,500,500,fill="midnight blue",width=0)#create sky
c.create_rectangle(0,200,500,500,fill="lawn green",width=0)#create grass
c.create_rectangle(100,50,400,150,fill="MediumPurple2",width=0)#create roof shape1
c.create_polygon(400,50,400,150,475,150,fill="MediumPurple2",width=0)#create roof shape2
c.create_polygon(100,50,25,150,175,150,width=0,fill="dark violet")#create black shade roof shape3

c.create_rectangle(25,150,175,400,fill="blue violet",width=0)#create home front
c.create_rectangle(175,150,475,400,fill="medium purple",width=0)#create home back

c.create_oval(70,100,120,140,outline="",fill="yellow")#main window

c.create_arc(50,570,150,230,start=0,extent=180,style="chord",outline="",fill="OrangeRed4")#door
c.create_arc(75,300,125,250,start=45,extent=90,style="pieslice",outline="",fill="yellow")
c.create_arc(75,305,120,250,start=140,extent=40,style="pieslice",outline="",fill="yellow")
c.create_arc(80,305,125,250,start=0,extent=40,style="pieslice",outline="",fill="yellow")
c.create_oval(65,310,80,325,outline="",fill="salmon4")#doorknob

c.create_rectangle(200,200,450,250,width=0,fill="aquamarine2")#create back window
