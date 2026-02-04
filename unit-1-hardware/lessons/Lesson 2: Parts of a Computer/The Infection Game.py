# The following link for the infection game from teacher IF you wanna check it out, it's not my work it's his instead: https://codehs.com/sandbox/josephwaters/12-infection-game
import random
import time
import math

spreadRate = 2.5

canadaPop = 38250000
infected = 1
day = 0

dailyFunding = 100000

hospitalBudget = 0
socialHandBudget = 0

def choicePicker():
      global hospitalBudget
      global socialHandBudget
      
      dailyOption = int(input())

      if dailyOption == 1:
        hospitalBudget +=1    
      elif dailyOption == 2:
        socialHandBudget += 1
      else:
        print("Please type either 1 or 2.")
        choicePicker()

print("A new highly infectious disease (infection rate of 2-3)")
print("has been discovered and has begun infecting Canadians.")
print()
print("You, the Canadian Government, need to use your funding")
print("to keep this disease in check.")
print()
print("Try to eradicate the disease, and don't let Canada's")
print("whole population (38,250,000) become infected.")
print()
input("Hit enter to continue...")
print()

while infected > 0 and infected < canadaPop:

  print ("-"*23)
  print ("Day",day,"of the Outbreak")
  print ("-"*23)
  print ("There are currently",infected,"infected individuals")

  hospitalRate = hospitalBudget * hospitalBudget * 100
  socialHandRate = 1 - (math.sqrt(socialHandBudget) * 0.2)

  day += 1       
  spreadVariance = .5 - random.random()  
  dailySpread = max([1.1,(spreadRate * socialHandRate) + (spreadVariance)])
  infected = round(infected * dailySpread) - hospitalRate

  print("Current rate of infection is", round(dailySpread,2))

  if day >= 7:
    
    if day == 7:
      print()
      print("The government decides to take action.")
    
    print()
    print("Your daily funding is: $",dailyFunding,sep="")
    print("How do you wish to spend it?")
    print("1: Hospital Building (Cures the Infected)")
    print("2: Social Distancing and Hand Washing Info Campaign (Lowers the Infection Rate)")
    
    choicePicker()

    print()
    print("***Current Funding Allocation***")
    print("Hospitals: $",(dailyFunding * hospitalBudget),sep="")
    print("Social Distancing and Hand Washing: $",(dailyFunding * socialHandBudget),sep="")

  print('\n' * 2)

  time.sleep(1.5)

if infected >= canadaPop:
  print ("Everyone in Canada is infected.")
  print("--Game Over--")
else:
  print ("Everyone in Canada is cured.")
  print("--You Win--")
