import turtle

speed(0)
distance = 50
t = turtle.Turtle()


sides = int(input("Tell me, how many sides does this shape have? "))

while sides == 0 or sides == 2 or sides <= 0:
    print("You must be out of your gourd!")
    sides = int(input("now tell me how many sides this shape have? "))
    
goto(0,0)

concentric = int(input("How many concentric copies do you want? "))
if sides == 1:
    t.circle(distance)
    
turn_angle = 360/sides

# we need to keep looping through the amount of concentric shapes and making them
# we don't need to be afraid of sides = 0 or 2, we checked that earlier!
if sides > 1:
    for e in range(concentric):
        for i in range(sides):
            t.forward(distance)
            t.left(turn_angle)
            
        distance += 25
            
