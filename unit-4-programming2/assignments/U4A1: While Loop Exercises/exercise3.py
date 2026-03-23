# 2 types of patterns

# Our imports
from turtle import *
import random

# Variables
x = 100
sub = 5
rounds = 0 
speed(2)
color('blue')

# First pattern, uncomment to see
#while rounds < 20:
#    forward(x - sub)

#    right(90)

#    forward(x - sub)

#    right(90)
    
#    rounds += 1
#    sub += 5
#    print(f"rounds: {rounds}")
#    print(f"subs: {sub}")
    


# Second pattern Random pattern generator
while rounds < 20:
    random_pattern = random.randint(4,10)
    angle = random.randint (0,360)
    move = random.randint (10,70)
    for i in range(random_pattern):
        forward(move)
        right(angle)
        
    rounds += 1
        
mainloop()
