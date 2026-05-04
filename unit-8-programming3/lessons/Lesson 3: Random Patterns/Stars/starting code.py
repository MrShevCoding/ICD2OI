###WARMUP###
#Using this starter file, create a starfield of 100 randomly placed stars in the sky.
#############

from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

screen.create_rectangle(0, 500, 800, 600, fill="dark green")

#First, how could you make the single star appear in a random position?
#Second, how do you make 100 appear?
#Finally, can you make the star size random as well?
starX = 400
starY = 300
screen.create_oval(starX, starY, starX+5, starY+5, fill="white") #star of width 5 pixels at starX, starY

#BONUS: Can you make each star a random colour, either red, yellow, white, or gray?


screen.mainloop()
