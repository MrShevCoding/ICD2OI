# Our imports
import random 

# Our variable
list = ["Heads", "Tails"]
score = 0
status = ""

# Ask user how many times to flip coin.
user_input = int(input("How many time would you like to flip the coin? "))

for i in range(user_input):
    flip = random.choice(list)
    
    # On heads add 1 to score
    if flip == "Heads":
        score += 1
        status = "you get 1 point!"
    
    # On tails don't add but still inform user
    if flip == "Tails":
        status = "you get nothing this time."
        
    print(f"The coin was {flip}, {status}")
    
# After everything
print(f"Your total score was {score}")
