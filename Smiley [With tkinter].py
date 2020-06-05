from tkinter import *
root=Tk()
c=Canvas(root,height=600,width=600)
c.pack()
c.create_oval(50,50,550,550,fill="yellow",outline="")#creating face
c.create_oval(160,160,250,250,fill="white",width=0)#creating eyebase
c.create_oval(185,165,250,230,fill="blue violet",outline="")#creating pupil
c.create_oval(200,185,215,200,fill="white",width=0)#creating light

c.create_oval(330,160,420,250,fill="white",width=0)#creating eyebase
c.create_oval(355,165,420,230,fill="blue violet",outline="")#creating pupil
c.create_oval(370,185,385,200,fill="white",width=0)#creating light

c.create_arc(200,200,380,400,start=180,extent=180,outline="",style="pieslice",fill="red2")
#making the mouth

c.create_polygon(220,300,250,300,235,340,fill="white",outline="")#creating a tooth
c.create_line(220,280,220,330,fill="cyan",width=2)#creating tooth spark
c.create_line(200,300,240,300,fill="cyan",width=2)
c.create_line(205,290,235,310,fill="cyan",width=2)
c.create_line(235,290,205,310,fill="cyan",width=2)

c.create_oval(100,270,180,300,fill="HotPink1",width=0)
c.create_oval(400,270,480,300,fill="HotPink1",width=0)
#creating blush

c.create_rectangle(260,440,330,480,fill="medium blue",outline="")
#create square of bowtie

c.create_polygon(260,440,100,390,100,540,260,480,fill="navy",width=0)#leaves of bowtie
c.create_polygon(330,440,500,390,500,540,330,480,fill="navy",width=0)

