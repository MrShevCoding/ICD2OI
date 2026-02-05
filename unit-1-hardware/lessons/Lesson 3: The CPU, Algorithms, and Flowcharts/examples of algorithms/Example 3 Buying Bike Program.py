#########################################################################
# Title:  An Algorithm For Buying a Bike Within a Budget
# Purpose:  To show how a simple, real-life algorithm can be programmed
# Last modified on:  7 February, 2020
# Programmer:  Mr. Schattman (not my work, this is the teacher's example of an algorithm)
#########################################################################

from time import *


#PRICES OF 8 DIFFERENT BICYCLES
prices = [ 3000, 1200, 700, 1000, 1400, 900, 800, 500, 412]

#WHETHER I LIKE EACH BIKE OR NOT
likeIt = [ "yes", "yes", "no", "no", "yes", "yes", "yes", "yes", "no" ]

#MY BUDGET FOR BUYING A BIKE
budget = float(input("How much are you willing to spend on a bike? $"))


#THIS LOOP GOES THROUGH EACH BIKE IN THE LIST
numBikes = len(prices)

for i in range( numBikes ):  

    currentPrice = prices[i] 
    
    if likeIt[i] == "yes":   #IF I LIKE THE CURRENT BIKE, DO THE FOLLOWING
        
        if currentPrice <= budget: #IF THE PRICE IS WITHIN MY BUDGET, PRINT THIS
            print ("BUY BIKE NUMBER " + str(i+1) + "! I like it, and $" + str(currentPrice), "is within my budget.")
            break
        
        else:  #BUT IF THE PRICE IS TOO HIGH, PRINT THIS
            print ("I like bike number", i + 1, "but $", currentPrice, "is too expensive")
            

    else:   # BUT IF I DON'T LIKE THE BIKE, PRINT THIS
        print ("I don't like bike number", i + 1)

    sleep(1) #PAUSE 1 SECOND BEFORE MOVING ON TO THE NEXT BIKE IN THE LIST
