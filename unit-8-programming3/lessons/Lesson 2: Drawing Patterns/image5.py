#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()

s.create_oval(350,50,450,150,fill='yellow')
s.create_line(400,100,400,450,fill='yellow')

x=0
for i in range(24):
    s.create_line(400,100,400+x,450,fill='yellow')
    x+=23

x=0
for i in range(24):
    s.create_line(400,100,400-x,450,fill='yellow')
    x+=23

s.mainloop()
