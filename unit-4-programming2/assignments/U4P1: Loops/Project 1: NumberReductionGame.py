# Project 1: Number reduction game
# We let the user pick between doing a 1v1 against bot or up to 4 seprate player
# It's turn-based between all of the players where their goal is to reach 0
# They can either /2 or -1 the number


# Our imports
import time
 
# Made this cool function that if a person types 'stats' anywhere (well anywehere i put it in the code below)
# it displays the current number and the players turns, it returns true so that it can be re-prompted
# otherwise return false and keep going
def check_stats(c):
    if c == "stats":
        print()
        print(f" Current number : {number}")
        print(f" Current player move : {current_player}")
        print()
        time.sleep(0.2)
        return True
    return False
 
# Oh before hand, if you see the code below v
print()
time.sleep(0.4)
# It just helps make the console look pretty/more readible and makes the game feel more alive!



# Another function that helps controll the game, it repeatedly prints to the the user
# until they enter one of the valid_choices strings (comparison is case-insensitive).


# Also able to intercepts 'stats' at any prompt so players can
# always check the game state without losing their turn.

def safe_input(prompt, valid_choices):

    while True:
        c = input(prompt).lower()          # normalise to lowercase helps us out
 
        if check_stats(c):                 # 'stats' shows the info and lets them re-prompt
            continue
 
        if c in valid_choices:             # if the answer is valid then we can return it
            return c
 
        # Everything else the input is invalid, this is where we
        # tell the player exactly what's expected from them
        print(f"  Invalid input. Please choose from: {', '.join(valid_choices)}")
        time.sleep(0.2)
 
 
# Printing user welcoming
print("   Welcome to the Number Reduction Game!")
time.sleep(0.3)
 
# Ask if the player wants to hear the rules
# safe_input handles the y/n validation and the 'stats' shortcut
hear_rules = safe_input(
    "Do you want to hear the rules first? (y/n): ",
    ["y", "n"]
)
print()
time.sleep(0.2)
 
# Print the rules only if the user has said they wanted to
if hear_rules == "y":
    print("-" * 25)
    print("THE RULES")
    print("-" * 25)
    time.sleep(0.2)
    print("-> 1. Player 1 picks any whole number greater than 1.")
    time.sleep(0.3)
    print("-> 2. Players take turns reducing the number by:")
    time.sleep(0.3)
    print("---> Subtracting 1,  OR")
    time.sleep(0.3)
    print("---> Halving it where it's rounded down.")
    time.sleep(0.3)
    print("-> 3. The first player to reach 0 wins!")
    time.sleep(0.3)
    print("-" * 25)
    print()
    time.sleep(0.3)
 
# Fianlly after all of that we get number of players
# safe_input validates only we accept "1","2","3","4" as strings
print("How many players will be playing?")
print("-> (Enter 1 to play against the bot, or 2-4 for multiplayer)")
print()
 
time.sleep(0.3)
print()
# We use strings here so safe_input can compare them directly,
# then convert the result to int afterwards for later arithmetic math
player_count = int(safe_input(
    "Number of players (1/2/3/4): ", ["1", "2", "3", "4"]
))
print()
time.sleep(0.2)
 
# Decide whether the bot mode is turned on only after we have a validated value
if player_count == 1:
    bot_mode = True
    player_count = 2   # the bot is always Player 2 internally
    print("Alright! You'll be playing against the bot.")
    print("Good luck, i'm just saying I made it to play pretty smart!")
else:
    bot_mode = False
    print(f"Nice! Setting up a {player_count} player game.")
    print("Have fun you all, can't wait to see the result.")
 
print()
time.sleep(0.4)
 
# Get the starting number from P1
# Numbers can't go through safe_input directly (it works with strings),
# so we handle this with a manual loop and int() conversion.
print("-" * 25)
print("Player 1 gets to choose the starting number.")
print()
 
# Initialise to a value that will fail validation on the first check
number = 0
current_player = 1   # initialise here so check_stats() can reference it later
 
# We keep looping and make sure that the user inputs a number greater than 2
while number <= 2:
    # We use try because we want to TRY this because if a user inputs something wrong or something that would cause an error
    # the program will still try it despite issue might poping up for it
    try:
        # Get our input
        current_input = input("Player 1, enter a starting number greater than 2: ").strip().lower()
        print()
        time.sleep(0.2)
 
        # Allow 'stats' even at the starting-number prompt
        if current_input == "stats":
            check_stats(current_input)
            continue

        # We now convert to int() to help with math, like the check below
        number = int(current_input)

        # If the user input a number that is less or greater than 2
        if number <= 2:
            print("The number must be greater than 2. Try again!")

    # If we receives an argument that has the correct type but an inappropriate value, then we print to user
    except ValueError:
        # Player typed something that isn't a number at all
        print("Please enter a whole number greater than 2.")
 
print(f"Great! Starting number is {number}. Let the game begin!")
print("-" * 45)
print()
time.sleep(0.5)
 
 
print("psst, quick tip, type 'stats' at any prompt to see")
print("the current number and whose turn it is right now.")
print()


# Player 1 both picks the number and also goes first in the reductions
current_player = 1
 
# We keep looping while the number is greater than 0, or basically until someone gets to zero
while number > 0:
 
    # Calculate the two possible moves for this turn
    subtract_choice = number - 1   # Option A: subtract 1
    half_choice     = number // 2  # Option B: halve and round down
 
    # Checks if both options are identical which means only one real move exists
    if subtract_choice == half_choice:
        if subtract_choice == 0:
            # That move wins the game, announce it and stop the game
            print(f"Player {current_player}, your only choice is 0, so YOU WIN!")
            print()
            time.sleep(0.4)
            print("*" * 25)
            print(f"   *** Player {current_player} wins! Congratulations! ***")
            print("*" * 25)
            time.sleep(0.4)
            break
        else:
            print(f"Player {current_player}, your only choice is {subtract_choice}.")
    else:
        print(f"Player {current_player}, your choices are {subtract_choice} or {half_choice}.")
 
    time.sleep(0.3)
 
    # Bot turn (always Player 2 in bot mode if player picked 1 player)
    if bot_mode and current_player == 2:
        # Strategy: halve when even (shrinks number fastest) and
        # subtract when it's odd (halving an odd number just does n-1 anyway).
        if number % 2 == 0:
            move = half_choice
        else:
            move = subtract_choice
 
        print(f">> Bot chose: {move}")
        print()
        time.sleep(0.5)
 
    # Human player turn
    else:
        # Build the list of valid string choices for safe_input
        if subtract_choice == half_choice:
            valid = [str(subtract_choice)]
        else:
            valid = [str(subtract_choice), str(half_choice)]
 
        # safe_input will keep re-prompting on bad input and will
        # also handle 'stats' if someone used it mid-turn
        move = int(safe_input(
            f"Enter your move ({' or '.join(valid)}): ", valid)
            )
        print()
        time.sleep(0.2)
 
    # After 1 round, we need to update the overall number 
    number = move
 
    # Check if anyone has a win 
    if number == 0:
        print(f"  Player {current_player} reached 0!")
        time.sleep(0.3)
        print()
        print("*" * 25)
        print(f"   *** Player {current_player} wins! Congratulations! ***")
        print("*" * 25)
        time.sleep(0.4)
        break
 
    # Advance to the next player (wraps back to 1) 
    current_player += 1
    if current_player > player_count:
        current_player = 1
 
    print()  
 
# Game Over happens at the very end
print()
print("Thanks for playing the Number Reduction Game!")
print("=" * 25)
