# this isn't mine but still an example: https://codehs.com/sandbox/josephwaters/23-multi-step-algorithms

print ("Welcome to my fraction adder!")

#Input fractions from the user
n1 = int(input("Enter the first fraction's numerator: "))
d1 = int(input("Enter the first fraction's denominator: "))
n2 = int(input("Enter the second fraction's numerator: "))
d2 = int(input("Enter the second fraction's denominator: "))

#Calculate numerator and denominator for two temporary fractions with a common denominator
newN1 = n1 * d2
newD1 = d1 * d2 
newN2 = n2 * d1
newD2 = d2 * d1

#Output the temporary fractions to the user
print ("Fraction 1 is now: ", newN1, "/", newD1)
print ("Fraction 2 is now: ", newN2, "/", newD2)

#Add the new numerators
finalN = newN1 + newN2

#Output the final answer
print("The answer is: ", finalN, "/", newD2)
