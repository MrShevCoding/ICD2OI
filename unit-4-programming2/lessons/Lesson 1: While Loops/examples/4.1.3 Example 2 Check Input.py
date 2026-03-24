#ASK THE FIRST TIME
school = input("Enter your school:")


#MAKE THE USER RE-ENTER THE GRADE UNTIL IT'S A VALID RESPONSE
while school not in ["LHSS", "BCI", "ECI"]:
  print("Invalid response!")
  school = input("Enter your school:")


#DO SOMETHING USEFUL WITH THE USER'S RESPONSE, NOW THAT WE'RE CERTAIN IT'S VALID
print("Wow! I hear everyone at", school,"is a nerd!")
