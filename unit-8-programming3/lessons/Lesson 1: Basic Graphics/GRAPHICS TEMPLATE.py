#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()

#
#
#Your code goes here
#
#


#Grid lines
#REMOVE THESE BEFORE SUBMITTING ANY ASSIGNMENTS
spacing = 50

for x in range(0, 800, spacing): 
    screen.create_line(x, 25, x, 600, fill="white")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

for y in range(0, 600, spacing):
    screen.create_line(25, y, 800, y, fill="white")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")

screen.mainloop()
