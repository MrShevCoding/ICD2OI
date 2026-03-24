# You don't have to do this but it looks funny seeing the aggressiv moos :)
import time

# Write a for-loop that prints:
#                       The cow says m
#                       The cow says mo
#                       The cow says moo
#                       The cow says mooo
#                       The cow says moooo
#                       The cow says mooooo
#                       The cow says moooooo

looping_time = int(input("How many times do you wish for the cow to moo? "))

# Problem: if the user asked to loop 10 times but what we saw earlier
# python doesn't include the finale number, so we just add 1
for i in range(looping_time + 1):
    amount_o = "o" * i
    
    print(f"m{amount_o}")
    
    # Some programs like c++ or low-level programming wait in milliseconds, but python waits in seconds
    time.sleep(0.05)
