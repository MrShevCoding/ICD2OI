########################################
# Title: Wave Motion
# Purpose: To illustrate how to make objects move in wave patterns
# Programmer:  Mr. Schattman
# Last modified:  March 13, 2015
########################################

from tkinter import *
from time import *
from math import *

tk = Tk()
s = Canvas(tk, width=1000,height=900,background="black")
s.pack()

spacing = 100
for x in range(0, 1200, spacing): 
    s.create_line(x, 50, x, 900, fill="white")
    s.create_text(x,5, text=str(x), font="Times 14", fill="white", anchor = N)

for y in range(0, 900, spacing):
    s.create_line(50, y, 1200, y, fill="white")
    s.create_text(5, y, text=str(y), font="Times 14", fill="white", anchor = W)

s.update()

blueBall=0
greenBall=0
r = 200

for f in range(5000):
    
    #Vertical oscillation, with no horizontal motion
    x1Y = 100
    y1Y = 100 + 50*sin( 0.06*f )  #what happens if you change the 200?  Or the 0.12?
    x2Y = x1Y + 20
    y2Y = y1Y + 20

    #Vertical oscillation WITH horizontal motion
    x1B = 5*f + 100
    y1B = y1Y #same y-formula as the red ball
    x2B = x1B + 20
    y2B = y1B + 20
    
    #Horizontal wave
    x1G = 600 + 200*sin( 0.12*f )
    y1G = 5*f + 100
    x2G = x1G + 20
    y2G = y1G + 20

    yellowBall = s.create_oval(x1Y, y1Y, x2Y, y2Y, fill="yellow")
    #blueBall = s.create_oval(x1B, y1B, x2B, y2B, fill="cyan", width=2)
    greenBall = s.create_oval(x1G, y1G, x2G, y2G, fill="green", width=2)  #UNCOMMENT THIS TO SEE THE HORIZONTAL WAVE

    s.update()
    sleep(0.03)
    s.delete( yellowBall )
    #s.delete( yellowBall )  #UNCOMMENT THIS TO JUST SEE THE BALL MOVING WITH NO TRAIL LEFT BEHIND
    #s.delete( greenBall )
    
