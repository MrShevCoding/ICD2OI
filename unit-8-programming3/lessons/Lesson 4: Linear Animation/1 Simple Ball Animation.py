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






# Below is just the same just for the third task for brick instead

# Comment this below when needed to see the first or vice versa with the upper
from tkinter import *
from time import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the Rect anchor points
Rectx1 = 100
Recty1 = 600


#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(300): 

    #Create the Rect using the anchor points
    redRect = s.create_rectangle(Rectx1 - 100,  Recty1,  Rectx1 + 100,  Recty1 + 100,  fill="red",  outline="black") 

    #Update to place the Rect on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0399)
    #Delete the Rect from the canvas
    s.delete(redRect)

    #Update the anchor points so the Rect's x position changes by 10 pixels for next cycle of loop
    Recty1 -= 10
