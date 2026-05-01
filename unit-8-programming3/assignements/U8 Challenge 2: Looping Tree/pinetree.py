#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()


s.create_polygon(0,0,800,0,800,600,0,600,fill='blue')
s.create_polygon(0,500,800,500,800,600,0,600,fill='white')

s.create_polygon(300,200,450,200,450,600,300,600,fill='brown')


y=0
x=0
for i in range(3):
    s.create_polygon(375,20+y/1.2,200-x,200+y,575+x,200+y,fill='green')
    x+=50
    y+=120


s.mainloop()
