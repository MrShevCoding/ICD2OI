# Imports
import random

speed(100)

# Our 2 lists, for shapes and colours
shapes = ["Square", "Triangle", "Pentagon"]
colours = ["Red", "Blue", "Green", "Yellow"]

# x is just a random item in the list, vice versa y for colours list
x = random.choice(shapes)
y = random.choice(colours)
color(y)

# If the random shape was square
if x == "Square":
    pendown()

  # Loop through each side of the shape, change color aswell
    for i in range(4):
        forward(90)
        right(90)
        y = random.choice(colours)
        color(y)
        
# If the random shape was triangle
if x == "Triangle":
    pendown()

  # Same comment as square, 3 sides
    for i in range(3):
        forward(90)
        left(120)
        y = random.choice(colours)
        color(y)


# If the random shape was a pentagon
if x == "Pentagon":
    pendown()

  # Loop through all 6 sides
    for i in range(6):
        forward(90)
        right(60)
        y = random.choice(colours)
        color(y)
