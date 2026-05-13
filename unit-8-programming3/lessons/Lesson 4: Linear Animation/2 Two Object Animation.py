from tkinter import *
from time import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the ball anchor points
redBallX1 = 100
redBallY1 = 100

blueBallX1 = 300
blueBallY1 = 0

#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(300): 
    
    #Create the balls using the anchor points
    redBall = s.create_oval(redBallX1, redBallY1,  redBallX1 + 100,  redBallY1 + 100,  fill="red",  outline="black")
    blueBall = s.create_oval(blueBallX1, blueBallY1,  blueBallX1 + 100,  blueBallY1 + 100,  fill="blue",  outline="black") 

    #Update to place the balls on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0333)
    #Delete the balls from the canvas
    s.delete(redBall, blueBall)

    #Update the anchor points so the balls' positions change for next cycle of loop
    redBallX1 = redBallX1 + 10
    blueBallY1 = blueBallY1 + 10



# Bellow is for task 4, my solution
# again comment the upper part if you want to see the lower part work and vice versa

from tkinter import *
from time import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the ball anchor points
redBallX1 = 100
redBallY1 = 100

blueBallX1 = 300
blueBallY1 = 0

#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(100): 
    
    #Create the balls using the anchor points
    redBall = s.create_oval(redBallX1, redBallY1,  redBallX1 + 100,  redBallY1 + 100,  fill="red",  outline="black")

    #Update to place the balls on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0333)
    #Delete the balls from the canvas
    s.delete(redBall)

    #Update the anchor points so the balls' positions change for next cycle of loop
    redBallX1 = redBallX1 + 10



#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(100): 
    
    #Create the balls using the anchor points
    blueBall = s.create_oval(blueBallX1, blueBallY1,  blueBallX1 + 100,  blueBallY1 + 100,  fill="blue",  outline="black") 

    #Update to place the balls on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0333)
    #Delete the balls from the canvas
    s.delete(blueBall)

    #Update the anchor points so the balls' positions change for next cycle of loop
    blueBallY1 = blueBallY1 + 10
    
    
