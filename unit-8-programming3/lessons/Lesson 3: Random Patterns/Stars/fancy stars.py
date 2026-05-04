###WARMUP###
#Using this starter file, create a starfield of 100 randomly placed stars in the sky.
#############

from tkinter import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=600, background="black")
s.pack()

s.create_rectangle(0, 500, 800, 600, fill="dark green")

#First, how could you make the single star appear in a random position?
#Second, how do you make 100 appear?
#Finally, can you make the star size random as well?



#BONUS: Can you make each star a random colour, either red, yellow, white, or gray?

amount_stars = randint(25,1000)

for i in range(amount_stars):
    starX = randint(0,750)
    starY = randint(0,467)
    raduis = randint(1,6)
    
    # Found this on https://stackoverflow.com/questions/22950997/random-fill-colour-for-shapes-in-pythontkinter
    # RGB formating
    de=("%02x"%randint(0,255))
    re=("%02x"%randint(0,255))
    we=("%02x"%randint(0,255))
    ge="#"
    color=ge+de+re+we


    s.create_oval(starX, starY, starX+raduis, starY+raduis, fill=color) #star of width 5 pixels at starX, starY



s.mainloop()
