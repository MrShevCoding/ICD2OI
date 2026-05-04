# This one was my 
#Initialize Tkinter with these
import random
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()

s.create_polygon(0,0,800,0,800,600,0,600,fill='blue')
s.create_rectangle(0,300,800,600,fill='green')
s.create_polygon(0,400,800,400,800,500,0,500,fill='black')


x=0
for i in range(15):
    s.create_line(0+x,450,50+x,450,fill='yellow',width=1)
    x+=67
    

s.create_oval()

s.mainloop()
