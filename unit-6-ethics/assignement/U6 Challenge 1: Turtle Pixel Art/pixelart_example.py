import turtle
bgcolor("Black")
speed(0)
pensize(1)

pixelSize = 15

#This defines a new command "square()"
#If you write "square()", python will do the following indented lines of code
def square(pcolor):
  begin_fill()
  for x in range(4):    
    color(pcolor)
    forward(pixelSize)
    right(90)
  end_fill()

#####
#KEEP THE ABOVE CODE. BELOW ARE EXAMPLES WHICH MAY BE DELETED
#####

#Example 1
#Drawing two squares, one yellow, one using a hex code for a shade of green
square("Yellow")
forward(pixelSize)
square("#34eb46")


penup()
forward(pixelSize)
forward(pixelSize)
pendown()


#Example 2
#Tetris Line Piece using a loop
for x in range(4):
  square("Blue")
  forward(pixelSize)
   

penup()
forward(pixelSize)
forward(pixelSize)
pendown()


#Example 3
#Tetris Square Piece
for x in range(4):
  square("Yellow")
  right(90)
