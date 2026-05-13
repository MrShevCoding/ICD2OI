#This program demonstrates the basic animation loop.
#We use a loop to draw an object, briefly pause, then delete that object.
#The object is moved slightly, then the process repeats.
#If done fast enough, the object appears to move smoothly across the canvas.

from tkinter import *
from time import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the ball anchor points
ballx1 = 100
bally1 = 100


#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(300): 

    #Create the ball using the anchor points
    redBall = s.create_oval(ballx1,  bally1,  ballx1 + 100,  bally1 + 100,  fill="red",  outline="black") 

    #Update to place the ball on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0333)
    #Delete the ball from the canvas
    s.delete(redBall)

    #Update the anchor points so the ball's x position changes by 10 pixels for next cycle of loop
    ballx1 = ballx1 + 10
