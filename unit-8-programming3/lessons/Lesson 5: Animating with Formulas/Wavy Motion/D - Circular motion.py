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


s.update()
redBall=0
greenBall=0
circleBall=0
line1=0
line2=0
x1 = 100

for f in range(5000):
    
    x1 = 100
    y1 = 400 + 300*cos( 0.05*f ) 
    x2 = x1 + 20
    y2 = y1 + 20

    redBall = s.create_oval(x1, y1, x2, y2, fill="red")

    x3 = 400 + 300*sin( 0.05*f ) 
    y3 = 100
    x4 = x3 + 20
    y4 = y3 + 20

    greenBall = s.create_oval(x3, y3, x4, y4, fill="green")

    line1 = s.create_line(x1+10, y1+10, x3+10, y1+10, fill="yellow", width=4)
    line2 = s.create_line(x3+10, y3+10, x3+10, y1+10, fill="yellow", width=4)
    
    circleBall = s.create_oval(x3, y1, x4, y2, fill="white")

    s.update()
    sleep(0.03)
    s.delete( greenBall, redBall, line1, line2 )
    #s.delete( circleBall )

    
