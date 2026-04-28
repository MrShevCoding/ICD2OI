# Was given by teacher as an example, we did modify things out and would reccomand you to do the same to see what changes.

from tkinter import*
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=600, background="LightBlue2" )
screen.pack()

signWords = input("Enter your name: ")
postWidth = int(input("How wide do you want the post? "))


#GRASSY BACKGROUND
screen.create_rectangle(0, 550, 800, 600, fill = "green4")

#SUN
screen.create_oval(600, 128, 700, 228, fill = "yellow")

#STOP SIGN
screen.create_polygon(200, 210, 300, 210, 400, 310, 400, 410, 300, 510, 200, 510, 100, 410, 100, 310, fill = "red")

#POST
screen.create_line(250, 510, 250, 600, fill = "gray50", width = postWidth)

#TEXT ON THE SIGN
screen.create_text(250, 365, text = signWords, font = "Arial 75", fill = "white")

#GRID LINES
spacing = 50 #you can change this number
for x in range(0, 800, spacing): 
    screen.create_line(x, 25, x, 600, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 600, spacing):
    screen.create_line(25, y, 800, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.mainloop()
