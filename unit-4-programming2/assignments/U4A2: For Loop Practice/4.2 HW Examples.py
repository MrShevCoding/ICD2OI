#--------------------------------
#Example 1 Simplest Possible Loop
#--------------------------------
#Try changing range(0, 5) to range(0, 8):

for x in range(0, 8):
  print( "Bye!", x )

#--------------------------------------------
#Example 2 Making Use of the Looping Variable
#--------------------------------------------
#We can use the looping variable to make tables of values,
#where the x-value is the looping variable, and the y-value can
#be any formula that uses the looping variable.

#for x in range(0,20):
#    y = 5*x
#    print(x, "\t",  y)

#----------------------------------------
#Example 3 Incrementing A String Variable
#----------------------------------------
#Try changing it to scream = scream + "A"

#scream = "AH"

#for letterCounter in range(0, 9):
#    scream = scream + "H"
#    print(scream)

#-----------------------------------------
#Example 4 Incrementing A Numeric Variable
#-----------------------------------------
#Try changing the monthly salary
#Try changing the starting value of totalEarnedSoFar to 20000 and also
#Change the plus sign in the formula to a minus sign

#from time import *

#total = 0
#salary = 4300

#for month in range(1, 13):

#    print("This is month #" + str( month ) )

#    total = total + salary #An increment statement
    
#    print( "You just earned another $" + str( salary ))
#    print( "SO FAR THIS YEAR YOU HAVE EARNED $" + str( total ))
#    print( "#"*20 )
#    print( "" )
    
#    sleep(1)
