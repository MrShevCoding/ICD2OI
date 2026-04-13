# Get our input
user_number = int(input("What's the number? "))
# Called a regex libary what we need
import re

# Variables
ans = 0
s = str(user_number)

# Keep looping, checking every number, is it slow YES, does it work, also yes lol
for i in range(0, user_number):

    # If the number that it looped either has a digit of 4 or 9, then true
    x = bool(re.match('^[49]+$', str(i)))

    # If true then add one to the answear
    if x == True:
        ans += 1

# Finally print everything
print(ans)

'''
^ : Start of string.
[49] : Character class matching '4' or '9'.
+ : Matches one or more of the preceding class.
$ : End of string.
'''


# Below was me trying to figure out a solution
#len_user_number = len(user_number)




# def find_fav_numbs(x):
#     y = 0
#     test_numb = 0
#     while x >= 0:
#         x -=  int(fav_numbs[y])
#         amount_numbs.append(fav_numbs[y])
#         print(amount_numbs)
#         print(x)
#         y+=1




# # if the number is a single digit
# print(fav_numbs[0]) # 2 possible

# # if the number is second digit
# print(fav_numbs[1]+fav_numbs[0]) # 4 possible

# # if the number is thrid digit
# print(fav_numbs[0]+fav_numbs[0]+fav_numbs[0]) # 8 possible

# # if the number is fourth digit
# print(fav_numbs[0]+fav_numbs[0]+fav_numbs[0]+fav_numbs[0]) # 16 possible


# # if the number have 5 digit -> 32 possible
# # if the numbe rhave 6 digit -> 64 possible
