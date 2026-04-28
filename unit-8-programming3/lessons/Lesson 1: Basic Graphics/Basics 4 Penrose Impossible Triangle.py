# Given by teacher, pretty cool stuff

from tkinter import *
interface=Tk()
screen=Canvas(interface, width=525, height=475, background="peru")
screen.pack()

#Penrose's Impossible Triangle
screen.create_polygon( 220,150, 40,475, 0,400, 220,0, 415,330, 322,330, fill="grey50", outline="black")

screen.create_polygon( 40,475, 220,150, 260,220, 160,400, 525,400, 485,475, fill="black")

screen.create_polygon( 220,0, 301,0, 525,400, 444,400, 160,400, 199,330, 405,330, fill="white", outline="black")

screen.create_line(220,1, 301,1, fill="black", width=3)

screen.mainloop()
