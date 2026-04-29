#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="red")
screen.pack()

#Semicircle (the "extent" is 180 degrees)
screen.create_arc( 50, 300, 250, 500, start=90, extent=180, fill="white")
#Same semicircle flipped upside down
screen.create_arc( 50, 300, 250, 500, start=90, extent=-180, fill="black")

screen.create_oval(100,300,200,400,fill="black",outline='black')
screen.create_oval(100,400,200,500,fill='white',outline="white")

screen.create_oval(125,425,175,475,fill='black')
screen.create_oval(125,325,175,375,fill='white',outline='white')

screen.mainloop()
