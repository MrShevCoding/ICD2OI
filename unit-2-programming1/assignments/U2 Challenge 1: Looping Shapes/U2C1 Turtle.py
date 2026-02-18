import random
speed(1000)

#Take this code and try to understand what it is doing.
#then, fork it (make a copy) and change it from a red square 
#that increases side length by 5 every cycle, to a blue octagon (8 sides) 
#that increases by 10 every cycle.
#Submit your work by copying the URL of your code and attaching it here.

sidelength = 10

for i in range(random.randint(33,76)):  # draw a rectangle, in this case a square (all sides equal to sidelength)
  color('red')
  forward(sidelength)
  left(90)
  forward(sidelength)
  left(90)  
  forward(sidelength)
  left(90)
  forward(sidelength)
  left(90)
  sidelength = sidelength + 5

penup()
goto(-100,-100)
sidelength = 1
color('blue')
pendown()

for q in range(random.randint(24,55)):
    for w in range(random.randint(10,40)):
        forward(sidelength)
        left(45)
    sidelength += 10
