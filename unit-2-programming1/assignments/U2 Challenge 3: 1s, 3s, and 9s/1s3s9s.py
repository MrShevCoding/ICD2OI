# Take a number from a user, and output how many 1s, 3s, and 9s would fit in that number.

number = int(input("What your number? "))

# We don't really need one, as the final number is the amount of 1
amount_9 = 0
amount_3 = 0

amount_9 = number//9

number -= amount_9*9

amount_3 = number//3

number -= amount_3*3

# Finally print
print(f"{amount_9} nine, {amount_3} three, {number} ones.")
