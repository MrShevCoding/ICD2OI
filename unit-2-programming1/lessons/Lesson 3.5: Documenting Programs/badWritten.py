# this isn't mine but an example: https://codehs.com/sandbox/josephwaters/235-badly-written?authuser=0

a = int(input("Enter the first fraction's numerator: "))
b = int(input("Enter the first fraction's denominator: "))
c = int(input("Enter the second fraction's numerator: "))
d = int(input("Enter the second fraction's denominator: "))
tempx = a * d
tempy = b * d 
tempz = c * b
temp4 = d * b
print ("Fraction 1 is now: ", tempx, "/", tempy)
print ("Fraction 2 is now: ", tempz, "/", temp4)
answer = tempx + tempz
print("The answer is: ", answer, "/", temp4)
