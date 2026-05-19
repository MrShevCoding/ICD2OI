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

r = 10
for f in range(5000):
    
    x1 = 400 + r*cos( 0.25*f ) 
    y1 = 400 + r*sin( 0.25*f ) 
    x2 = x1 + 20
    y2 = y1 + 20

    circleBall = s.create_oval(x1, y1, x2, y2, fill="yellow")

    s.update()
    sleep(0.03)
    #s.delete( circleBall )

    r = r+1 #try uncommenting this
