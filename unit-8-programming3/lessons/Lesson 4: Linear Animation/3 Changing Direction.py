from tkinter import *
from time import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the ball anchor points, and speed
ballx1 = 100
bally1 = 100
ballSpeedX = 10


#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(300): 


  ballx2 = ballx1 + 100
  bally2 = bally1 + 100
    #Create the ball using the anchor points
  redBall = s.create_oval(ballx1, bally1,  ballx2,  bally2,  fill="red",  outline="black") 

    #Update to place the ball on the canvas
  s.update()
    #Pause Python for a short amount of time
  sleep(0.0666)
    #Delete the ball from the canvas
  s.delete(redBall)
    
    #This checks if the edge of the ball has reached the right edge of the screen. 
    #If so, the ball speed becomes negative, making the ball switch directions. 
  if(ballx2 >= 800):
    ballSpeedX = ballSpeedX * -1

    #Update the anchor points so the ball's position changes for next cycle of loop
    #If ballSpeedX is positive, ball is moving right. 
    #If ballSpeedX is negative, ball is moving left.
  ballx1 = ballx1 + ballSpeedX




# The following day we were given a warm up exercies for dvd logo, did 
# everything was to lazy to do the dvd logo :p, again comment upper if want to see lower
from tkinter import *
from time import *
from random import*

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#Initialize the ball anchor points, and speed
ballx1 = 100
bally1 = 100
ballSpeedX = 10
ballSpeedY = 10


colors = ["Red", "Blue", "Green", "Cyan", "Orange", "Green", "White", "Blue"]

pick_color = choice(colors)


#Loop will run 300 times, each cycle being 1 frame of animation
for frames in range(300): 


  ballx2 = ballx1 + 100
  bally2 = bally1 + 100
    #Create the ball using the anchor points
  redBall = s.create_oval(ballx1, bally1,  ballx2,  bally2,  fill=pick_color,  outline="black") 

    #Update to place the ball on the canvas
  s.update()
    #Pause Python for a short amount of time
  sleep(0.0666)
    #Delete the ball from the canvas
  s.delete(redBall)
    
    #This checks if the edge of the ball has reached the right edge of the screen. 
    #If so, the ball speed becomes negative, making the ball switch directions. 
  if(ballx2 >= 800):
    ballSpeedX *= -1
    pick_color = choice(colors)
    
    
    
  if(ballx2 <= 0):
    ballSpeedX = abs(ballSpeedX)
    pick_color = choice(colors)
    
    
  if(bally2 >= 600):
     ballSpeedY *= -1
     pick_color = choice(colors)

     
  if(bally2 <= 0):
     ballSpeedY = abs(ballSpeedY)
     pick_color = choice(colors)


    #Update the anchor points so the ball's position changes for next cycle of loop
    #If ballSpeedX is positive, ball is moving right. 
    #If ballSpeedX is negative, ball is moving left.
  ballx1 += ballSpeedX
  bally1 += ballSpeedY
  
