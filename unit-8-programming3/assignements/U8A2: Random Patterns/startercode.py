from tkinter import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=600, background="black")
s.pack()

s.create_rectangle(0,500,800,600, fill="saddle brown")

#1
#PUMPKIN ANCHOR POINTS
#because all x and y points of the shapes that make up the pumpkin are based on these numbers
#changing these will move the entire pumpkin accordingly
pumAncX = 25
pumAncY = 450

#pumpkin body
s.create_oval(pumAncX, pumAncY, pumAncX + 50, pumAncY + 50, fill="orange")
#pumpkin stem
s.create_rectangle(pumAncX + 19, pumAncY - 10, pumAncX + 31, pumAncY, fill="saddle brown")
#pumpkin face
s.create_oval(pumAncX + 10, pumAncY + 10, pumAncX + 20, pumAncY + 20, fill="yellow")
s.create_oval(pumAncX + 30, pumAncY + 10, pumAncX + 40, pumAncY + 20, fill="yellow")
s.create_arc(pumAncX+10, pumAncY+10, pumAncX + 40, pumAncY + 40, fill="yellow", start = 180, extent = 180)


#2
#scarecrow post
s.create_line(550,500,550,450, width=10, fill="brown")
#scarecrow body
s.create_oval(525,350,575,450, fill="burlywood3")
#scarecrow arms
s.create_oval(500,385,525,415, fill="burlywood3")
s.create_oval(575,385,600,415, fill="burlywood3")
#scarecrow head
s.create_oval(525,300,575,350, fill="burlywood3")
s.create_oval(530,320,540,330, fill="yellow")
s.create_oval(560,320,570,330, fill="yellow")
s.create_arc(535,328,565,358, fill="yellow", start = 0, extent = 180)

s.mainloop()
