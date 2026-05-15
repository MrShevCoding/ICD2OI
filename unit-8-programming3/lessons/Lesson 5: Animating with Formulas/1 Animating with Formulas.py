from tkinter import *
from math import *
from time import *
root = Tk()
screen = Canvas(root, width=1200, height=1000, background="black")
screen.pack()

xGreen = 100
yGreen = 100

xRed = 0

d = 40 #diameter

for f in range(300):  
  #OLD METHOD Linear animation for green ball
  #Y Position increases by 5 pixels every frame
  yGreen = yGreen + 5

  #FORMULA METHOD Linear animation for the red ball 
  #Y position = starting position (100) plus 5 pixels per frame
  
  # Starts at y = 250 and has a speed of 3 pixels per frame
  yRed = 3*f + 250
  
  # New linear equation for xposition
  # Start at x = 100 and speed of 2 pixels per frame
  
  xRed = 2*f + 100

  greenBall = screen.create_oval( xGreen, yGreen, xGreen+d, yGreen+d, fill = "green" )
  redBall = screen.create_oval( xRed, yRed, xRed+d, yRed+d, fill = "red" )
  
  screen.update()
  sleep(0.03)
  screen.delete(redBall, greenBall)
