from tkinter import *

tk = Tk()
s = Canvas(tk, width=800,height=600, background="yellow")
s.pack()

#WARMUP
#Move the bear face to the middle of the canvas, WITHOUT tweaking the coordinate values individually
#HINT: Think back to our pumpkins and anchor points

Bx = 300
By = 250
#Bear face
s.create_oval(100 + Bx,50 + By,125 + Bx,75 + By,fill="blue")
s.create_oval(175 + Bx,50 + By,200 + Bx,75 + By,fill="blue")
s.create_polygon(120 + Bx,100 + By, 180 + Bx, 100 + By, 150 + Bx, 140 + By, fill="blue")
s.create_line(100 + Bx,175 + By, 200 + Bx,175 + By,fill="blue",width=10)

s.mainloop()
