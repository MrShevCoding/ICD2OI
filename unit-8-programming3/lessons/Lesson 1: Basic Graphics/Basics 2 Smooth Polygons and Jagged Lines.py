# Was given by our teacher, would reccomened to for anyone to expirment, also with the 2 lines trying change them :) 

from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="black")
screen.pack()

#A rectangle with only the border shown with no fill color
screen.create_rectangle( 120, 120, 240, 240, fill = "blue", outline = "coral", width=6)

#Jagged line
screen.create_line(0, 500, 100, 300, 200, 500, 300, 300, 400, 500, 500, 300, 600, 500, fill="green", width=3)

#Jagged line that's been "smoothed" out
screen.create_line(0, 500, 100, 300, 200, 500, 300, 300, 400, 500, 500, 300, 600, 500, fill="red", width=0.1, smooth=True)                    

#Create a polygon with "smoothed" edges
screen.create_polygon( 800,300,  450,50,  550,40,  550,0, fill="DodgerBlue", outline="hot pink", width=5, smooth=True)

#Actually places the new graphics created above onto the canvas
screen.update()


#GRID LINES FOR HELPING YOU PLAN THE SCENE
spacing = 50
for x in range(0, 1000, spacing): 
    screen.create_line(x, 20, x, 1000, fill="grey50")
    screen.create_text(x, 10, text=str(x), font="Times 10", anchor = N, fill="grey50")

for y in range(0, 1000, spacing):
    screen.create_line(30, y, 1000, y, fill="grey50")
    screen.create_text(5, y, text=str(y), font = "Times 10", anchor = W, fill="grey50")

screen.mainloop()
