
#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="black")
screen.pack()

# All 6 points to define the bluetooth logo
screen.create_polygon(300,200,370,220,370,430,300,450,220,430,220,220, fill="cyan",outline="blue",width=10,smooth=True)

# Line at the middle
screen.create_line(300,225,300,425,fill="black",width=8,smooth=True)

# The rune
screen.create_line(240,400,340,275,fill="black",width=8,smooth=True)
screen.create_line(240,250,340,375,fill="black",width=8,smooth=True)
screen.create_line(340,275,300,225,fill="black",width=8,smooth=True)

screen.create_line(340,375,300,425,fill="black",width=8,smooth=True)

screen.mainloop()

# Below were points i was testing to find the optimal bluetooth outline, was annyoing
#screen.create_oval(295,195,305,205, fill="red")
#screen.create_oval(295,445,305,455, fill="red")


#screen.create_oval(365,425,375,435, fill ="red")  
#screen.create_oval(215,425,225,435, fill = "red")

#screen.create_oval(365,215,375,225, fill ="red")
#screen.create_oval(215,215,225,225, fill="red")
