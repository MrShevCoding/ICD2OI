#The input() command treats whatever value the user typed 
#as a *text string*, even if they entered a number.
#If we want the user to enter a number, then we have to 
#wrap an int() command around the input statement, so that Python will 
#turn the text number into an actual number that can be use in later calculations.

#EXAMPLE 1: Input whole numbers
mark1 = int(input("Enter your 1st mark: ")) #We use int(input("...")) for WHOLE NUMBER inputs
mark2 = int(input("Enter your 2nd mark: "))

averageMark = (mark1 + mark2)/2
print(averageMark)

print("The average of", mark1, "and", mark2, "is", averageMark)



#EXAMPLE 2: Input decimal numbers
iPodPrice = float(input("Enter the price: "))  #We use float(input("...")) for DECIMAL inputs

HST = 0.13 * iPodPrice
total = iPodPrice + HST

HSTrounded = round(HST,2)
totalrounded = round(total,2)

print("HST not rounded: ", HST)
print("HST: ", HSTrounded)
print("Total due:", totalrounded)


####YOUR TURN###
#Let the user input their age. Then calculate how much older you are than them
#and print out that result.
