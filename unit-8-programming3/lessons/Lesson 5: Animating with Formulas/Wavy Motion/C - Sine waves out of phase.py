from tkinter import *
from math import *
from time import *


myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=600, background="black")
screen.pack()


#TRY CHANGING THESE
amplitude = 100
phaseShift = 20
numBalls = 30
f = .03
linesOn = False
colors = ["yellow","red","blue"]
numColors = 3


#CALCULATIONS
gap = 1000 / (numBalls)
r = max(gap / 5, 3)
numPeriods = 50

if linesOn == True and numBalls < 2000:
    for x in range (0, numBalls):
        screen.create_line( gap*x+r, 0, gap*x+r, 1000, fill="grey20")

y = []
ball = []
for b in range(0, numBalls):
    y.append(0)
    ball.append( screen.create_oval(0, 0, 1, 1, fill="black") )


#ANIMATION 
for angle in range ( 0, int(numPeriods * 360) ):
    
    for ballNum in range(0, numBalls):
        y[ ballNum ] = amplitude * sin( f*(angle - ballNum * phaseShift  ) ) + 300
        x1 = ballNum * gap
        y1 = y[ ballNum ]
        x2 = x1 + 2*r
        y2 = y1 + 2*r
        c = colors[ballNum % numColors]
        ball[ ballNum ] = screen.create_oval( x1, y1, x2, y2, fill=c, outline=c )

    screen.update()
    sleep(0.002)

    for ballNum in range(0, numBalls):
        screen.delete( ball[ ballNum ] )


    


    
    
