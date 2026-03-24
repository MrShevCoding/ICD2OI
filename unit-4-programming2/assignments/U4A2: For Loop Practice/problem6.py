# Write a for-loop that adds the first 20 whole numbers:  1 + 2 + 3 + … + 19 + 20 
# and prints the current sum after each new number is added.
#          The sum of the first 1 whole numbers is 1
#          The sum of the first 2 whole numbers is 3
#          The sum of the first 3 whole numbers is 6
#          The sum of the first 4 whole numbers is 10
#          The sum of the first 5 whole numbers is 15
#          etc.
list = []


# Python has this handy function called sum(), just adds
# All the items int he list together
for i in range(1,21):
    list.append(i)
    print(sum(list))
    
    
    
