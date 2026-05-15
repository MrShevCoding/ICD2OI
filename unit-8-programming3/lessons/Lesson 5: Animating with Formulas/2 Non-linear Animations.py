#Instead of using increment statements to animate objects, we can use formulas.
#Formulas let us animate more interesting motion, such as parabolas

from tkinter import *
from math import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=600, background="black")
screen.pack()

greenBallSize = 40
greenXPos = 300

redBallSize = 40
redXPos = 400

for frame in range(300):

  #This is a linear function (y = m*x +b)
  #The y position increases linearly every frame
  #This is similar to the movement we did with increment
  
  # Initial height of 100, initial speed of 15, and UPWARD
  # accelaration of 0.25
  redYPos = (-0.25 * frame**2) + (15 * frame) + 100

  #This is a quadratic fuction (y = a*x^2 + b*x + c)
  #The y position moves in a parabolic motion
  #We could not normally do this with increment statements
  #a = gravity strength (0.5), b = initial velocity(-10),
  #c = starting position (200)
  greenYPos = 0.5 * frame**2 - 10 * frame + 200  

  greenball = screen.create_oval(greenXPos, greenYPos, greenXPos + greenBallSize, greenYPos + greenBallSize, fill = "green" )

  redball = screen.create_oval(redXPos, redYPos, redXPos + redBallSize, redYPos + redBallSize, fill = "red" )
  
  screen.update()
  sleep(0.03)
  screen.delete(greenball, redball)
