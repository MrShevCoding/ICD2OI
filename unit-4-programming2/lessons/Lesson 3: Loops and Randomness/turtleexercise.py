penup()

# Up most right corner of the screen
goto(-175,175)

pendown()
for i in range(5):
    
    # Across
    forward(150)
    right(90)
    
    # Lil indent
    forward(25)
    
    # Going backwards
    forward(-25)
    left(90)
    forward(-150)
    
    # Next line
    right(90)
    forward(25)
    left(90)
