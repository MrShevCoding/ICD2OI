#Instead of using increment statements to animate objects, we can use formulas.
#Formulas let us animate more interesting motion, such as parabolas

from tkinter import *
from math import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=600, background="white")
screen.pack()

bowlingBallSize = 40
bowlingBallXPos = 300


for frame in range(300):

  #This is a linear function (y = m*x +b)
  #The y position increases linearly every frame
  #This is similar to the movement we did with increment
  
  # Initial height of 100, initial speed of 15, and UPWARD
  # accelaration of 0.25
  bowlingBallYPos = (0.25 * frame**2) + (15 * frame) + 100

  bowlingBall = screen.create_oval(bowlingBallXPos, bowlingBallYPos, bowlingBallXPos + bowlingBallSize, bowlingBallYPos + bowlingBallSize, fill = "orange" )
  
  screen.create_line(0,420,800,420,fill='black')
  if bowlingBallYPos >= 400:
      bowlingBallYPos = 400
      sleep(2)
  else:    
      screen.update()
      sleep(0.03)
      screen.delete(bowlingBall)
