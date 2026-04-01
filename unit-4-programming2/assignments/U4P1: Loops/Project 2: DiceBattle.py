# Project 2, using python console, we make a text-based roguelike dice battle game built
# the player fights an AI bot until one of them reaches a target score the player sets at the start
 

# Below explains more on the core gameplay of this chaotic game
# - Both sides roll dice every round
# - Higher roll gains points equal to the difference between the two rolls
# - Random rooms can appear after battles:
#       Shop        -> buy upgrades with your points
#       Reforge     -> forge special dice or upgrade existing ones
#       Trade Room  -> swap one stat for another
#       Gamble Room -> bet your points on a coin flip basically
# - Theirs a chance for you and the bot to get a random upgrade drops with a rarity system (common up to legendary)
# - After 10 rooms, the area can change with negative biome effects
# - 3 starter classes (Heavy, Sniper, Rogue), each with their own playstyle
# - Special forge dice you can unlock:
#       Doubler    -> chance to double your roll
#       Punisher   -> damages the bot's score when you win a round
#       Minimizer  -> raises your minimum roll
#       Streak     -> bonus points for win streaks
#
# The player can also write the items below without interupting their turn:
# -> Type "p stats" anywhere to view your full player stats
# -> Type "b stats" anywhere to view the bot's current stats
# -> safe_input() is used everywhere so typos won't crash or break your run


# Our imports
import random
import time

# All of the variables are needed before the function below or else they wouldn't work
# Setting up all the player variables and stats before the game starts
# These get modified throughout the run by drops, rooms, and area effects
player_score = 0
player_dice_max = 6     # the highest number we can roll
minimum_roll = 1        # the lowest number we can roll
player_multiplier = 1   # multiplies the points we gain each win
player_luck = 0         # increases drop rarity and gamble odds
player_regen = 0        # free points added to our score every round
crit_chance = 0         # percent chance to add +3 to our roll



# Special forge dice, all start as off/False until bought in the Reforge room
has_doubler = False       # chance to double our roll
has_punisher = False      # removes points from bot on a win
has_minimizer = False     # pushes minimum roll up to half of max die
winstreak_enabled = False # streak dice, gives bonus points for consecutive wins

# Levels for dice that can be upgraded in the Reforge room
doubler_level = 1
punisher_level = 1
streak_level = 1
win_streak = 0   # tracks how many rounds in a row we've won


# The bot is simpler than the player but it can still get upgrade drops
# which would keep a good level of threat even in later rounds
bot_score = 0
bot_dice_max = 6
bot_multiplier = 1

# bot_bonus_crit resets every round so we need a separate variable that
# actually persists between rounds
# When the bot earns a crit drop, it goes into bot_crit_stored
# Then each round we add bot_crit_stored into bot_bonus_crit before rolling
# So yes, the bot getting a crit can be very high at some moments which is awesome
bot_crit_stored = 0

round_number = 1
# This function checks if the user typed a stats command instead of a real answer
# If they did, we print out the stats and return True so the caller knows to re-prompt
# If they didn't, we just return False and let things carry on normally
def check_stats(command):
    command = command.lower()

    if command == "p stats":
        print()
        print("=" * 25)
        print("YOUR STATS")
        print("=" * 25)
        print(f"  Score: {player_score}")
        print(f"  Die Range: {minimum_roll} to {player_dice_max}")
        print(f"  Multiplier: x{player_multiplier}")
        print(f"  Luck: {player_luck}")
        print(f"  Regen: {player_regen}")
        print(f"  Crit Chance: {crit_chance}%")
        print(f"  Win Streak: {win_streak}")
        print(f"  Doubler: {has_doubler}  (Lv {doubler_level})")
        print(f"  Punisher: {has_punisher}  (Lv {punisher_level})")
        print(f"  Minimizer: {has_minimizer}")
        print(f"  Streak Dice: {winstreak_enabled}  (Lv {streak_level})")
        print("=" * 25)
        print()
        time.sleep(0.3)
        return True

    elif command == "b stats":
        print()
        print("=" * 25)
        print("BOT STATS")
        print("=" * 25)
        print(f"  Score: {bot_score}")
        print(f"  Die Range: 1 to {bot_dice_max}")
        print(f"  Multiplier: x{bot_multiplier}")
        print(f"  Bot stored crit: {bot_crit_stored}%")
        print("=" * 25)
        print()
        time.sleep(0.3)
        return True

    return False


# Same safe_input we used in project 1, keeps looping until the user enters
# something valid, also lets them check stats mid prompt without losing their turn
def safe_input(prompt, valid_choices):
    while True:
        c = input(prompt).lower()

        if check_stats(c):   # if they typed stats, show it and re-prompt
            continue

        if c in valid_choices:   # valid answer, we're good to go
            return c

        # if we got here the input was no good, tell them what to pick
        print(f"Invalid input. Please choose from: {', '.join(valid_choices)}")
        time.sleep(0.2)


# Starting the game
print()
time.sleep(0.2)
print("WELCOME TO DICE BATTLE")
time.sleep(0.2)
print("=" * 25)
print()
time.sleep(0.3)
print("psst you can type 'p stats' or 'b stats' at any")
print("prompt during the game to check stats!")
print()
time.sleep(0.3)

# Ask if the user wants the rules before we do anything else
see_rules = safe_input("Do you want to see the rules? (y/n): ", ["y", "n"])
print()
time.sleep(0.2)

if see_rules == "y":
    print("-" * 25)
    print("THE RULES")
    print("-" * 25)
    time.sleep(0.2)
    print("-> Both you and the bot roll a die each round.")
    time.sleep(0.2)
    print("-> Whoever rolls higher gains points equal")
    print("to the difference between the two rolls.")
    time.sleep(0.2)
    print("-> First to hit the target score you set wins.")
    time.sleep(0.2)
    print("-> Random rooms appear between rounds with")
    print("upgrades, shops, trades, and gambles.")
    time.sleep(0.2)
    print("-> Upgrade drops can land after any round,")
    print("with rarity ranging from Common to Legendary.")
    time.sleep(0.2)
    print("-> Special dice can be forged in the Reforge room.")
    time.sleep(0.2)
    print("-> Each area has a biome effect that changes")
    print("how the round plays out...")
    time.sleep(0.2)
    print("-" * 25)
    print()
    time.sleep(0.3)

# We let the player set the target score themselves so they can pick a short
# or long run depending on how much time they have
while True:
    # Like project 2, we need to try this because a wrong input might cause error and python no like
    try:
        target_score = int(input("What score do you want to play to? (recommended: 50-200): "))
        print()
        time.sleep(0.2)
        if target_score <= 0:
            print("Score has to be greater than 0, try again!")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

print(f"Okey than, first to {target_score} points wins. Let's go!")
print()
time.sleep(0.4)

# give player access to 3 starter classes
# Each class gives the player a different starting advantage so
# runs feel different depending on what style you're going for
print("-" * 25)
print("  Choose your starter class:")
print()
time.sleep(0.2)
print("  1 = Heavy   -> starts with +2 max die (bigger rolls)")
time.sleep(0.2)
print("  2 = Sniper  -> starts with +16% crit chance (chance to increase you roll)")
time.sleep(0.2)
print("  3 = Rogue   -> starts with +1 minimum roll (floor is higher)")
print()
time.sleep(0.3)

starter_class = safe_input("  Pick your class (1/2/3): ", ["1", "2", "3"])
print()
time.sleep(0.2)

# Map the choice to a readable class name for display later
if starter_class == "1":
    class_name = "Heavy"
elif starter_class == "2":
    class_name = "Sniper"
else:
    class_name = "Rogue"

print(f"Nice pick! You're running it as a {class_name}.")
time.sleep(0.2)
print("Get ready to battle...")
print("-" * 25)
print()
time.sleep(0.5)




# Apply the class bonus right away before any rounds start
if class_name == "Heavy":
    player_dice_max += 2
elif class_name == "Sniper":
    crit_chance += 16
elif class_name == "Rogue":
    minimum_roll += 1

# Special areas only start in after round 10, before that its just Regular
# Each area is short (3-5 rounds) to keep the the moment intense
# The area list is shuffled so every run feels different
# Each tuple is (name, length_in_rounds)
special_areas = [
    ("Grass Field",  4),
    ("Lava Lagoon",  3),
    ("Ice Canyon",   4),
    ("Dark Cave",    3),
    ("Heavy Swamp",  3),
    ("Barren Desert",4),
    ("Storm Peaks",  3),
    ("Ancient Ruins",4),
]

# We shuffle the order so each run feels different
random.shuffle(special_areas)

# area_queue is what we actually pull from during the game
# Regular lasts the first 10 rounds, then special areas start after in one by one
area_queue = [("Regular", 10)] + special_areas

area_index = 0
area_round = 0   # how many rounds we've been in the current area
current_area, area_length = area_queue[area_index]

# ominous_shown makes sure the "you feel an ominous path" message only prints once
ominous_shown = False

# Print the area effects reference so the player isn't flying blind
print("AREA EFFECTS GUIDE (most areas punish you!):")
print("-> Grass Field  : you regen +1 per round (only friendly area)")
print("-> Lava Lagoon  : bot +30% crit AND your min roll drops by 1")
print("-> Ice Canyon   : bot regens +2 AND your multiplier drops by 1")
print("-> Dark Cave    : bot gets +20% crit, darkness hurts not helps")
print("-> Heavy Swamp  : min roll drops by 2, eats your regen too")
print("-> Barren Desert: drains regen every round, +1 luck barely helps")
print("-> Storm Peaks  : max die shrinks by 2 AND bot gets +25% crit")
print("-> Ancient Ruins: your multiplier up but bot max die grows permanently")
print()
time.sleep(0.5)

print("Starting in: Regular  (first 10 rounds are safe... for now...)")
print()
time.sleep(0.3)


# Our main game loop
# We keep going until someone hits the target score
while player_score < target_score and bot_score < target_score:

    print("=" * 25)
    print(f"ROUND {round_number}  |  AREA: {current_area}")
    print(f"Your Score: {player_score}  |  Bot Score: {bot_score}")
    print(f"Target: {target_score}  |  Die: {minimum_roll}-{player_dice_max}")
    print("=" * 25)
    print()
    time.sleep(0.2)

    # Wait for the player to press enter so they control the pace of the game
    # We still check for stats commands here in case they need to
    while True:
        roll_command = input("Press enter to roll (or type 'p stats'/'b stats'): ").lower()

        if check_stats(roll_command):
            continue
        break

    print()
    time.sleep(0.3)

    # Reset the per-round bot bonuses before applying area effects
    # These only last one round so they have to be cleared each time
    # bot_crit_stored is not reset here however, that one persists across rounds on purpose
    bot_bonus_crit = 0 + bot_crit_stored   # carry over any stored crit the bot earned from drops
    bot_bonus_regen = 0
    player_bonus_regen = 0

    # Apply the current area biome effect on top, there meant to be punishing!
    # Most areas heavily favour the bot so the player actually has to fight through them
    if current_area == "Grass Field":
        # Only mild positive area, a small breather between the rough ones
        player_bonus_regen = 1
        print("You stumble upon a large green grass field, you feel a sigh of relief..")
        print("-> You regen +1 this round. Enjoy it, won't last you forever.")

    elif current_area == "Lava Lagoon":
        # Bot gets a huge crit boost and the heat tanks your min roll
        bot_bonus_crit += 30
        minimum_roll = max(1, minimum_roll - 1)
        print("During your roam, you fall and become stuck in a lava corridor, you feel the heat...")
        print(f"-> Bot has +30% crit AND your min roll dropped to {minimum_roll}.")
        print("-> The heat is getting to you...")

    elif current_area == "Ice Canyon":
        # Bot regens double and your multiplier is frozen at 1 for the round
        bot_bonus_regen = 2
        player_multiplier = max(1, player_multiplier - 1)
        print("You wondered to far and found yourself in a cold tundra...")
        print(f"-> Bot regens +2. Worse, your multiplier drops by 1 this round.")
        print("-> The cold is slowing you down.")

    elif current_area == "Dark Cave":
        # Cave only boosts the bot's crit, the darkness helps them not you
        bot_bonus_crit += 20
        print("You stumble upon a cave, you a brave soul enter, bad idea it's pitch black...")
        print(f"-> Something in the dark. Bot gains +20% crit.")
        print("-> You can barely see your own dice.")

    elif current_area == "Heavy Swamp":
        # Swamp tanks your min roll hard and permanently eats a point of regen if you have it
        minimum_roll = max(1, minimum_roll - 2)
        print("You somehow walk into a bog with no plan, weird but you head on...")
        if player_regen > 0:
            player_regen -= 1
            print(f"-> Min roll dropped to {minimum_roll} and 1 regen got lost in the mud.")
        else:
            print(f"-> Min roll dropped to {minimum_roll}. You are sinking.")

    elif current_area == "Barren Desert":
        # Desert drains regen every round it lasts, luck is now pratically gone
        player_luck += 1
        print("The long journey brought you to a naked desert, the wind howls each step...")
        if player_regen > 0:
            player_regen -= 1
            print(f"-> Regen drained by the heat (-1). Luck up to {player_luck} though.")
        else:
            print(f"-> Brutal sun. Luck up to {player_luck} but you are fading.")

    elif current_area == "Storm Peaks":
        # Storm cuts your max die and gives the bot a massive crit window
        player_dice_max = max(minimum_roll + 1, player_dice_max - 2)
        bot_bonus_crit += 25
        print("Among the mountains, you feel a storm surround all of your senses...")
        print(f"-> Lightning shaved your max die to {player_dice_max}.")
        print(f"-> Bot also has +25% crit. This one is rough.")

    elif current_area == "Ancient Ruins":
        # Ruins raises your multiplier but permanently boosts the bot die
        player_multiplier += 1
        bot_dice_max += 1
        print("Ancient ruins roaming and gloom over you, they set you unease, but whatever...")
        print(f"-> Your multiplier up to x{player_multiplier}, but bot max die now {bot_dice_max} permanently.")
        print("-> The ruins empower both sides, but the bot benefits more over time.")

    # Minimizer effect: if we have it, floor is pushed up to half the max die
    if has_minimizer:
        minimum_roll = max(minimum_roll, player_dice_max // 2)
        print(f"Your minimum roll is now {minimum_roll}.")

    print()
    time.sleep(0.3)

    # Roll the player's die within the current min/max range
    player_roll = random.randint(minimum_roll, player_dice_max)

    # Check for a crit, streak adds extra crit chance on top of the base
    total_crit = crit_chance + (win_streak * 2)

    if random.randint(1, 100) <= total_crit:
        player_roll += 3
        print("CRITICAL HIT! Your roll gets +3!")
        time.sleep(0.2)

    # Check if the Doubler fires, higher level means higher trigger chance
    if has_doubler and random.randint(1, 100) <= 20 + (doubler_level * 5):
        player_roll *= 2
        print(f"DOUBLER activated! Roll doubled!")
        time.sleep(0.2)

    # Roll the bot's die
    bot_roll = random.randint(1, bot_dice_max)

    # Bot crit check, the bot_bonus_crit already includes any stored crit from drops
    if random.randint(1, 100) <= bot_bonus_crit:
        bot_roll += 3
        print("Bot landed a CRIT! +3 to their roll!")
        time.sleep(0.2)

    # Show both rolls
    print(f"You rolled  : {player_roll}")
    print(f"Bot rolled  : {bot_roll}")
    print()
    time.sleep(0.4)

    diff = player_roll - bot_roll

    # Figure out who won the round and apply the points to the winners
    if diff > 0:
        gained = diff * player_multiplier
        player_score += gained
        print(f"You win the round! +{gained} points.")

        # Streak dice adds bonus points for each consecutive win the player got
        if winstreak_enabled:
            win_streak += 1
            bonus = win_streak * streak_level
            player_score += bonus
            print(f"STREAK x{win_streak}! Bonus +{bonus} points.")

        # If they have Punisher, it cuts a little bit points off the bot when we win
        if has_punisher:
            punish = (gained // 3) * punisher_level
            bot_score = max(0, bot_score - punish)
            print(f"PUNISHER activated! Bot loses {punish} points.")

    # Else if the difference is negative meaing the bot won thise time
    elif diff < 0:
        loss = abs(diff) * bot_multiplier
        bot_score += loss
        win_streak = 0   # reset streak on a loss
        print(f"Bot wins the round. They gain {loss} points.")
        if win_streak == 0 and winstreak_enabled:
            print("Your win streak was reset back to 0.")

    # Else out of all of that, it's a tie
    else:
        print("It's a tie! No points change hands.")

    # Apply passive regen after the round result, both sides
    player_score += player_regen + player_bonus_regen
    bot_score += bot_bonus_regen

    if player_regen + player_bonus_regen > 0:
        print(f"Regen kicks in: +{player_regen + player_bonus_regen} for you.")

    print()
    print(f"SCORES  ->  You: {player_score}  |  Bot: {bot_score}  |  Target: {target_score}")
    print()
    time.sleep(0.4)

    # check if the game has finished
    
    # stop immediately before drops / rooms if someone reached target
    if player_score >= target_score or bot_score >= target_score:
        break
    
    # Theirs a chance for players and bots to get upgrades after fight
    # we do this twice, one for the bot and on for the player
    # After every round there's a chance a random upgrade drops
    # Luck increases the chances of hitting higher rarities
    roll = random.randint(1, 100)

    if roll <= 2 + player_luck:
        rarity = "LEGENDARY"
        bonus_amount = 3
    elif roll <= 8 + player_luck:
        rarity = "EPIC"
        bonus_amount = 2
    elif roll <= 20 + player_luck:
        rarity = "RARE"
        bonus_amount = 2
    elif roll <= 40 + player_luck:
        rarity = "COMMON"
        bonus_amount = 1
    else:
        rarity = None   # no drop this round, most common outcome
        
    # If the rarity is active, we print telling players they got it
    if rarity is not None:
        print(f">={rarity} DROP!<=")
        time.sleep(0.3)

        # Pick a random upgrade type from the pool
        reward = random.choice(["luck", "regen", "crit", "dice", "multiplier"])

        # If that reward was luck, players luck increase
        if reward == "luck":
            player_luck += bonus_amount
            print(f"->[P1] Luck +{bonus_amount}  (now {player_luck})")


        # If that reward was regen, players regen increase
        elif reward == "regen":
            player_regen += bonus_amount
            print(f"->[P1] Regen +{bonus_amount}  (now {player_regen} per round)")

        # If that reward was crit, players crit increase
        elif reward == "crit":
            crit_gain = 5 * bonus_amount
            crit_chance += crit_gain
            print(f"->[P1] Crit Chance +{crit_gain}%  (now {crit_chance}%)")

         # If that reward was dice, players max die increase
        elif reward == "dice":
            player_dice_max += bonus_amount
            print(f"-> Max Die +{bonus_amount}  (now rolling up to {player_dice_max})")

        # If that reward was multiplier, players multiplier increase
        elif reward == "multiplier":
            player_multiplier += bonus_amount
            print(f"->[P1] Multiplier +{bonus_amount}  (now x{player_multiplier})")

        print()
        time.sleep(0.3)

    # Bot has a smaller one because well the area mass buff him
    # The bot has a much smaller drop chance than the player (12% vs player's luck-scaled rate)
    # but it can still get upgrades to stay a threat throughout the run
    bot_drop_roll = random.randint(1, 100)

    if bot_drop_roll <= 12:
        print("[BOT] The bot found an upgrade...")
        time.sleep(0.3)

        bot_reward = random.choice(["dice", "multiplier", "regen", "crit"])

        # If the bot got a dice, + 1 max
        if bot_reward == "dice":
            bot_dice_max += 1
            print(f"[BOT] Max Die +1  (now rolling up to {bot_dice_max})")

        # If the bot got a mutliplier, + 1 multipler
        elif bot_reward == "multiplier":
            bot_multiplier += 1
            print(f"[BOT] Multiplier +1  (now x{bot_multiplier})")

        # If the bot got a regen, + 1 regen
        elif bot_reward == "regen":
            bot_score += 2
            print(f"[BOT] Regen triggered, +2 instant score.")

        # If the bot got a crit, + 5 crit stored
        elif bot_reward == "crit":
            # This now goes into bot_crit_stored so it actually persists into future rounds
            # Before the fix this went into bot_bonus_crit which gets wiped every round
            bot_crit_stored += 5
            print(f"[BOT] Crit +5% stored permanently. Bot crit is now {bot_crit_stored}%.")

        print()
        time.sleep(0.3)



    # After the drop check there's a chance a special room appears
    # Rooms are where the real strategy happens, spend wisely!
    # Room spawn is much rarer, only 35% total chance per round
    room_roll = random.randint(1, 100)

    if room_roll <= 10:
        # Spend your points to buy permanent upgrades
        print("-" * 25)
        print("=== SHOP ===")
        print(f"Your current score: {player_score}")
        print()
        time.sleep(0.2)
        print("1 = +1 max die      (costs 6 points)")
        print("2 = x2 multiplier   (costs 8 points)")
        print("3 = regen +1        (costs 6 points)")
        print("4 = crit +10%       (costs 7 points)")
        print("5 = skip shop")
        print()

        c = safe_input("Pick an option: ", ["1", "2", "3", "4", "5"])

        # If the players want to buy +1 Max dice
        if c == "1":
            if player_score >= 6:
                player_score -= 6
                player_dice_max += 1
                print(f"Bought! Max die is now {player_dice_max}.")
            else:
                print("Not enough points for that (need 6).")

        # If the players want to buy x2 multiplier 
        elif c == "2":
            if player_score >= 8:
                player_score -= 8
                player_multiplier *= 2
                print(f"Bought! Multiplier is now x{player_multiplier}.")
            else:
                print("Not enough points for that (need 8).")

        # If the players want to buy more regen 
        elif c == "3":
            if player_score >= 6:
                player_score -= 6
                player_regen += 1
                print(f"Bought! Regen is now {player_regen} per round.")
            else:
                print("Not enough points for that (need 6).")

        # If the players want to buy more crit chance 
        elif c == "4":
            if player_score >= 7:
                player_score -= 7
                crit_chance += 10
                print(f"Bought! Crit chance is now {crit_chance}%.")
            else:
                print("Not enough points for that (need 7).")

        # They don't want to buy anything
        elif c == "5":
            print("Skipped the shop.")

        print("-" * 25)
        print()
        time.sleep(0.3)

    elif room_roll <= 18:
        # This is where you forge or upgrade the special dice
        print("-" * 25)
        print("=== REFORGE ROOM ===")
        print(f"Your current score: {player_score}")
        print()
        time.sleep(0.2)
        print("1 = Forge Doubler    (costs 10) -> chance to double your roll")
        print("2 = Forge Punisher   (costs 12) -> damages bot score on your wins")
        print("3 = Forge Minimizer  (costs 14) -> raises your roll floor")
        print("4 = Forge Streak     (costs 10) -> bonus points for win streaks")
        print("5 = Upgrade a die    (costs  8) -> level up a die you already have")
        print("6 = Skip")
        print()

        c = safe_input("Pick an option: ", ["1", "2", "3", "4", "5", "6"])

        # If the player wants to get chance double their roll
        if c == "1":
            if player_score >= 10:
                player_score -= 10
                has_doubler = True
                print(f"Doubler forged! (Lv {doubler_level})")
            else:
                print("Not enough points for that (need 10).")
            
        # If the player wants to get a die that punishes the bot
        elif c == "2":
            if player_score >= 12:
                player_score -= 12
                has_punisher = True
                print(f"Punisher forged! (Lv {punisher_level})")
            else:
                print("Not enough points for that (need 12).")
                
        # If the player want to get a die that raises your minimum
        elif c == "3":
            if player_score >= 14:
                player_score -= 14
                has_minimizer = True
                print("Minimizer forged! Your floor will rise.")
            else:
                print("Not enough points for that (need 14).")
        
        # If the player wants to get a die that get's them a streak
        elif c == "4":
            if player_score >= 10:
                player_score -= 10
                winstreak_enabled = True
                print(f"Streak Dice forged! (Lv {streak_level})")
            else:
                print("Not enough points for that (need 10).")

        # Or they just want to upgrade their current die
        elif c == "5":
            if player_score >= 8:
                # Only show the dice the player actually owns
                owned = []
                if has_doubler:
                    owned.append("1")
                if has_punisher:
                    owned.append("2")
                if winstreak_enabled:
                    owned.append("3")

                if not owned:
                    print("You don't have any special dice to upgrade yet.")
                else:
                    player_score -= 8
                    print("Which die do you want to upgrade?")
                    if has_doubler:
                        print(f"1 = Doubler  (currently Lv {doubler_level})")
                    if has_punisher:
                        print(f"2 = Punisher (currently Lv {punisher_level})")
                    if winstreak_enabled:
                        print(f"3 = Streak   (currently Lv {streak_level})")
                    print()

                    u = safe_input("Pick one: ", owned)

                    if u == "1" and has_doubler:
                        doubler_level += 1
                        print(f"Doubler upgraded to Lv {doubler_level}!")
                    elif u == "2" and has_punisher:
                        punisher_level += 1
                        print(f"Punisher upgraded to Lv {punisher_level}!")
                    elif u == "3" and winstreak_enabled:
                        streak_level += 1
                        print(f"Streak upgraded to Lv {streak_level}!")
            else:
                print("Not enough points for that (need 8).")

        elif c == "6":
            print("Skipped the reforge room.")

        print("-" * 25)
        print()
        time.sleep(0.3)

    elif room_roll <= 26:
        # Swap one stat for another, good for pivoting your build
        print("-" * 25)
        print("=== TRADE ROOM ===")
        print()
        time.sleep(0.2)
        print("Trade one stat away to boost another:")
        print(f"1 = crit -> multiplier  (you have {crit_chance}% crit, need 10%+)")
        print(f"2 = multiplier -> luck  (you have x{player_multiplier}, need more than 1)")
        print(f"3 = regen -> dice       (you have {player_regen} regen, need 1+)")
        print("4 = skip")
        print()

        t = safe_input("Pick an option: ", ["1", "2", "3", "4"])

        # If they want to exchange their crit for multiplier
        if t == "1":
            if crit_chance >= 10:
                crit_chance -= 10
                player_multiplier += 1
                print(f"Traded 10% crit for +1 multiplier.  (x{player_multiplier} now)")
            else:
                print("You need at least 10% crit to make that trade.")
        
        # If they want to exchange their multipler for luck
        elif t == "2":
            if player_multiplier > 1:
                player_multiplier -= 1
                player_luck += 2
                print(f"Traded 1 multiplier for +2 luck.  (luck is now {player_luck})")
            else:
                print("Your multiplier is already at 1, can't go lower.")
        
        # If they want to exhange their regen for max die
        elif t == "3":
            if player_regen >= 1:
                player_regen -= 1
                player_dice_max += 2
                print(f"Traded 1 regen for +2 max die.  (now rolling up to {player_dice_max})")
            else:
                print("You need at least 1 regen to make that trade.")

        # There too broke or too lazy and skip room
        elif t == "4":
            print("Skipped the trade room.")

        print("-" * 25)
        print()
        time.sleep(0.3)

    elif room_roll <= 35:
        # Bet some of your score on a 50/50 (luck can tilt it in your favour)
        # If the player has 0 points we skip it entirely so they don't get softlocked
        print("-" * 25)
        print("=== GAMBLE ROOM ===")
        print(f"Your current score: {player_score}")
        print()
        time.sleep(0.2)

        if player_score <= 0:
            # Nothing to bet so we just boot them out with a message
            print("You have no points to bet. The dealer turns you away.")
            print("Come back when you've got something to lose!")
        else:
            print(f"Your luck: {player_luck}  (adds to your win chance!)")
            print()
            print("Enter how many points you want to bet.")
            print("Win -> score goes up by that amount.")
            print("Lose -> score goes down by that amount.")
            print("Type 0 to walk away without betting.")
            print()

            # We use a manual loop here since the input is a freeform number, not a fixed set
            while True:
                g = input("How much do you want to bet? (0 to skip): ").lower()

                if check_stats(g):
                    continue

                # Check if their input is an actual digit
                if g.isdigit():
                    g = int(g)
                    
                    # They bet nothing
                    if g == 0:
                        print("You walked away. Smart move.")
                        break
                    
                    # They bet something greater then 1 and lower then their max score
                    elif 1 <= g <= player_score:
                        win_chance = 50 + player_luck
                        print(f"Betting {g} points at {win_chance}% win chance...")
                        time.sleep(0.5)
                        if random.randint(1, 100) <= win_chance:
                            player_score += g
                            print(f"YOU WIN! +{g} points. Score is now {player_score}.")
                        else:
                            # They lost the bet!
                            player_score -= g
                            print(f"You lose... -{g} points. Score is now {player_score}.")
                        break
                    else:
                        print(f"Bet has to be between 1 and {player_score}, or 0 to leave.")
                else:
                    print("Enter a whole number.")
                time.sleep(0.2)

        print("-" * 25)
        print()
        time.sleep(0.3)


    # Area progression below, it Count this round toward the current area's length
    # Once we hit the area's round limit, we move to the next one
    area_round += 1

    if area_round >= area_length:
        # Move to the next area in the queue
        # If we've used all special areas, cycle back through the shuffled list
        area_index += 1

        if area_index >= len(area_queue):
            # Ran out of areas, reshuffle and loop back through specials again
            random.shuffle(special_areas)
            area_queue[1:] = special_areas
            area_index = 1   # skip Regular, we already did that

        current_area, area_length = area_queue[area_index]
        area_round = 0

        # Before we announce the new area, check if we should show the
        # ominous message this them triggers exactly once right before the
        # first special area (after round 10)
        if not ominous_shown and current_area != "Regular":
            ominous_shown = True
            print()
            print("...")
            time.sleep(0.8)
            print("You feel an ominous path ahead of you...")
            time.sleep(0.8)
            print("Be strong...")
            time.sleep(1.0)
            print()

        # Now announce the area entry with its length and exactly what it does
        print()
        print("~" * 25)
        print(f"You stumbled upon {current_area}!")
        print(f"Hang on for {area_length} rounds.")
        print()
        time.sleep(0.3)

        # Print exactly what changed for both sides so the player always knows
        if current_area == "Grass Field":
            print("-> You : regen +1 each round here")
            print("-> Bot : no change")

        elif current_area == "Lava Lagoon":
            print("-> You : [DEBUFF] min roll drops by 1 each round here")
            print("-> Bot : [BUFF] +30% crit chance each round here")

        elif current_area == "Ice Canyon":
            print("-> You : [DEBUFF] multiplier drops by 1 each round here")
            print("-> Bot : [BUFF] regen +2 each round here")

        elif current_area == "Dark Cave":
            print("-> You : no buff")
            print("-> Bot : [BUFF] +20% crit chance each round here")

        elif current_area == "Heavy Swamp":
            print("-> You : [DEBUFF] min roll drops by 2 each round, regen drained if you have any")
            print("-> Bot : no change")

        elif current_area == "Barren Desert":
            print("-> You : [DEBUFF] regen drained each round, luck +1 as a consolation")
            print("-> Bot : no change")

        elif current_area == "Storm Peaks":
            print("-> You : [DEBUFF] max die shrinks by 2 each round here")
            print("-> Bot : [BUFF] +25% crit chance each round here")

        elif current_area == "Ancient Ruins":
            print("-> You : [BUFF] multiplier +1 each round here")
            print("-> Bot : [BUFF] max die permanently grows by 1 each round here")

        print("~" * 25)
        print()
        time.sleep(0.6)

    round_number += 1


# Game is over, print a proper summary of how the run went
print()
print("=" * 25)
print("FINAL RESULTS")
print("=" * 25)
print(f"Rounds played  : {round_number - 1}")
print(f"Your score     : {player_score}")
print(f"Bot score      : {bot_score}")
print(f"Target was     : {target_score}")
print()
time.sleep(0.3)

# If the player's score was greater then the bot's
if player_score >= target_score:
    print("YOU WIN! Great run!")
    print()
    print(f"Final stats -> Die: {minimum_roll}-{player_dice_max}")
    print(f"            -> Multiplier: x{player_multiplier}")
    print(f"            -> Crit Chance: {crit_chance}%")
    print(f"            -> Luck: {player_luck}")
    print(f"            -> Regen: {player_regen}")
# Else the bot won, sad
else:
    print("Bot wins this time. Better luck next run!")
    print(f"The bot finished with a {bot_dice_max} max die")
    print(f"and a x{bot_multiplier} multiplier.")
    
# Quick outro
print()
print("=" * 25)
print("Thanks for playing Dice Battle!")
print("=" * 25)
