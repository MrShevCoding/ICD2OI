#Try changing the monthly salary

from time import *

total = 0
salary = 4300

for month in range(1, 13):

  print("This is month #" + str( month ) )

  total = total + salary #An increment statement
  
  print( "You just earned another $" + str( salary ))
  print( "SO FAR THIS YEAR YOU HAVE EARNED $" + str( total ))
  print( "#"*20 )
  print( "" )
  
  sleep(3)
