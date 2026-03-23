# Math quiz! We add 2 random numbers together, as the user
# to guess them and if they get it write add 50, if not -1 lives

# Import random
from random import *

# Variables for later usage
score = 0
lives = 3
hardness = 0
rounds = 0

# While we have more lives than 0
while lives > 0:
    
    # Get 2 random values
    randomX = randint(1,100 + hardness)
    randomY = randint(1,100 + hardness)
    
    # Our answer for the 2 values
    rightAnswer = randomX + randomY
    
    # Printing for User
    print(f"Your current score: {score}")
    print(f"Your current lives: {lives}")
    print(f"current round: {rounds}")
    
    # There input/guess
    userGuess = int(input("What's " + str(randomX) + " + " + str(randomY) + "? "))
    
    # If they got it correctly
    if userGuess == rightAnswer:
        print("You got it!")
        print("")
        score += 50
        rounds += 1
        hardness = 5**rounds
        print(hardness)
    
    # Else they got it wrong
    else:
        print("Wrong!")
        print("")
        lives -= 1
        rounds += 1

# When the user runs out of lives
if lives == 0:
    print(f"You ran out of lives, your final score was {score}")
