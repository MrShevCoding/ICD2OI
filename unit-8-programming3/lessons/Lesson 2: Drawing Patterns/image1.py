#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()


screen.create_line(400,300,800,0, fill='white')

y=0
for i in range(6):
    screen.create_line(400,300,800,0+y,fill='white')
    y+=120

screen.mainloop()
