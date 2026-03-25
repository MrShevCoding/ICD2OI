from random import *

gameChoices = ["Rock", "Paper", "Scissors", "Tank", "Missile", "Feather"] #square brackets

for x in range(1,11):
    computersPick = choice( gameChoices )   #"choice" uses round brackets
    print( "The computer picked " + computersPick )
