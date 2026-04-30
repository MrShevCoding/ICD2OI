#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()

x=0
for i in range(20):
    s.create_line(0,0,0+x,400,fill='red')
    x+=12
    
s.mainloop()
