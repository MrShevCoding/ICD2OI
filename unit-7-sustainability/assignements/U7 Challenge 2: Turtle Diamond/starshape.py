import tkinter as tk


# 1. Setup the Tkinter s
root = tk.Tk()
root.title("Image from URL")
s = tk.Canvas(root, width=800, height=600)
s.pack()

movex = 0
movey = 0


# the only thing is noted is we move down the y value and add to the x value
# and add, subtract depending on the 4 little sections, try changing values for yourself!
for i in range(14):
    s.create_line(306,6 + movey,306 + movex,270,fill='red')
    movex += 22.5
    movey += 20
  
movex = 0
movey = 0
for i in range(14):
    s.create_line(306,6 + movey,306 + movex,270,fill='red')
    movex -= 22.5
    movey += 20
    
    
movex = 0
movey = 0
for i in range(14):
    s.create_line(306 + movex,270,306,550 - movey,fill='red')
    movex -= 22.5
    movey += 20
    
    
movex = 0
movey = 0
for i in range(14):
    s.create_line(306 + movex,270,306,550 - movey,fill='red')
    movex += 22.5
    movey += 20


root.mainloop()
