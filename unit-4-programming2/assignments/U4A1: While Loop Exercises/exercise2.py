# Write a program that has a number from 1–100 randomly chosen in the code –
# the magic number—and makes the user keep guessing until they get it right,
# but gives the user the following helpful feedback after every wrong guess:
import random

# Our variables
magic_numb = random.randint (0,100)
guess_status = False
guess_left = 5

# While the user hasn't guess correctly
while guess_status == False:
    
    # Grab input
    player_input = int(input("What's your guess? "))
    
    # Check this first to maake sure they can't kee playing
    if guess_left == 0:
        print("You ran out of guesses")
        print(f"the answear was {magic_numb}")
        exit()
        
        
    # If user guess too low
    if player_input < magic_numb:
        print("Nope! Too low.")
        guess_left -= 1
        print(f"You only have {guess_left} guess left.")
        
    # If the user guess too high
    if player_input > magic_numb:
        print("Nah, too high.")
        guess_left -= 1
        print(f"You only have {guess_left} guess left.")
        
    # If the user actually got the right answear
    if player_input == magic_numb:
        print(f"You got it with only {guess_left} guess left!")
        guess_status = True
