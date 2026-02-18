#Read through the starter code and try to understand what it is doing.

#Then, add to the drawing by writing some new code. You must add at least:
#- A tree
#- One other object of your choice

#Once you finish, copy the url of your code and attach it as a link to this assignment. Then, hit submit both here and on CodeHS.
#as note from me, this uses python built in turtle module for it to work
import random
speed(32)


# lines with a hashtag in front are called comments
# Python ignores them when you hit "run"
# they are here to help you understand the code


# each line of code below is a command that Python will follow, one by one, from top to bottom
# some commands change the cursor color, move or turn the cursor, or other actions
# try adding to the drawing by writing your own commands at the bottom of the program


# draw a red square by telling the cursor to move and rotate
color('red')
forward(100)
left(90)
forward(100)
left(90)  
forward(100)
left(90)
forward(100)
left(90)

# move cursor up to top left corner
penup()
left(90)
forward(100)
pendown()

# draw the roof
color('black')
right(30)
forward(100)
right(120)
forward(100)

# move to the bottom left of the house
penup()
right(30)
forward(100)
right(90)
forward(75)
right(90)

# draw the door
pendown()
color('brown')
forward(50)
right(90)
forward(30)
right(90)
forward(50)

# move to the sky and draw the sun
color('yellow')
penup()
backward(200)
right(90)
forward(100)
pendown()

# draws a circle with the radius = the number in the brackets
color('yellow')
begin_fill()
circle(30)
end_fill()

# end_fill()

# now lets try to draw the ground
pensize(23)
left(90)
penup()
forward(200)
color('green')
pendown()
left(90)
forward(200)

# tree
penup()
left(270)
forward(45)
left(270)
forward(267)
left(270)


speed(10)


color('brown')
pendown()
forward(45)
color('green')

left(270)
forward(1)
begin_fill()
circle(33)
end_fill()
penup()


forward(185)
left(270)
forward(55)

goto(25,-100)

# for i in range(random.randint(5, 50))
    
pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "gray"]
def draw_petal():
    for i in range(2):
        circle(100, 60)
        left(120)
        
for x in range(30):
    y = 10
    speed(y*25)
    pendown()
    color(random.choice(colors)) 
    draw_petal()
    left(360 / 30)
    y += 1000
