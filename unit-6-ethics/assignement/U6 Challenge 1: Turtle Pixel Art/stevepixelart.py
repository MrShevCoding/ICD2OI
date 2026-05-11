# inspo from here: https://au.pinterest.com/pin/3377768467409892/

import turtle
bgcolor("Black")
speed(0)
pensize(1)

pixelSize = 20


goto(-167,180)

pendown()
color("white")
forward(160)
right(90)
forward(160)
right(90)
forward(160)
right(90)
forward(160)
right(90)
# #This defines a new command "square()"
# #If you write "square()", python will do the following indented lines of code
def square(pcolor):
  begin_fill()
  for x in range(4):    
    color(pcolor)
    forward(pixelSize)
    right(90)
  end_fill()



for i in range(8):
    square("#5f3c18")
    forward(pixelSize)
    
goto(-167,160)

for i in range(8):
    square("#5f3c18")
    forward(pixelSize)
    
goto(-167,140)

square("#5f3c18")
forward(pixelSize)

for i in range(6):
    square('#ce9f81')
    forward(pixelSize)
    
square("#5f3c18")
forward(pixelSize)

penup()
goto(-167,120)

for i in range(8):
    square("#ce9f81")
    forward(pixelSize)
    
penup()
goto(-167,100)


square("#ce9f81")
forward(pixelSize)
square("white")
forward(pixelSize)

square("#2d619f")
forward(pixelSize)

for i in range(2):
    square("#ce9f81")
    forward(pixelSize)

square("#2d619f")
forward(pixelSize)
square("white")
forward(pixelSize)
square("#ce9f81")
forward(pixelSize)


penup()
goto(-167,80)

for i in range(3):
    square("#ce9f81")
    forward(pixelSize)
for i in range(2):
    square("#9f6e40")
    forward(pixelSize)
    
for i in range(3):
    square("#ce9f81")
    forward(pixelSize)


penup()
goto(-167,60)

for i in range(2):
    square("#ce9f81")
    forward(pixelSize)
    

square("#5f3c18")
forward(pixelSize)

for i in range(2):
    square("#ce9f81")
    forward(pixelSize)
    

square("#5f3c18")
forward(pixelSize)

for i in range(2):
    square("#ce9f81")
    forward(pixelSize)
    
penup()
goto(-167,40)


for i in range(2):
    square("#ce9f81")
    forward(pixelSize)


for i in range(4):
    square("#5f3c18")
    forward(pixelSize) 
 
for i in range(2):
    square("#ce9f81")
    forward(pixelSize)  
    
    
    
    
goto(67,40)
