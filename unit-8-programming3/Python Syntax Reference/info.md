Here is a document outlining most of the programming tools we have learned for easy reference.

# **Table of contents**

[Print statements](#bookmark=kix.o3v4odksc526)  
[Input statements](#bookmark=kix.2vi1ik29idw5)  
[If-Else statements](#bookmark=kix.na46n7bdbe76)  
[If-Elif-Else statements](#bookmark=kix.5oi8rim3a5k2)  
[Math & rounding](#bookmark=kix.55du2cqj7g05)  
[Trig (sin, cos, asin, acos)](#bookmark=kix.rbl2seqc4hvm)  
[While-loops](#bookmark=kix.uybgfq0zakk)  
[For-loops](#bookmark=kix.vyi6hnhzt6s8)  
[Generating random numbers and random choices](#bookmark=kix.6f43exmg5xl6)  
[Graphics](#bookmark=kix.x4kfhdp7ev9a)  
[Python colours](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)  
[Animations](#bookmark=kix.elx0dunadvlr)  
[Arrays](#bookmark=kix.hqgmghs0n87p)  
[Grabbing parts of strings](#bookmark=kix.952t4n69zt9d)  
[Functions & procedures](#bookmark=kix.bcaippo5glna)  
[Special string characters](#bookmark=kix.u7mejqhusz4)  
	

**Print statements**  
first Name \= "Akira"  
age \= 16  
favSport \= "battle golf"

**print**( "Hi, my name is"**,** firstName**,** "and I am"**,** age**,** "years old." )  
**print**( "I love to play"**,**  favSport **\+** "\!" )            *\#Use \+ sign when you don't want to print a space*  
**print**( "Yo, Akira, I'm also"**,**  **str**(age) **\+** "\!" )   *\#If the \+ sign joins text with a number, use **str***

**Input statements**  
*\#Entering words or text from the user*  
yourName \= **input**( "Enter your name:  ")  			  
yourCountry \= **input**( "Hi " **\+** yourName **\+** "\!  Where are you from? ") 

*\#Entering whole numbers*  
yourAge \= **int**(**input**( "How old are you? "))  	*\#Notice we need two ))'s at the end*	

*\#Entering decimals*  
cost \= **float**(**input**( "How much did your phone cost? "))	*\#Notice we need two ))'s at the end*

**If-else statements**  
likeCats \= **input**( "Do you like cats? ")

**if** likeCats \== "yes"**:**     *\#Use double-equals (==) to test a condition, but single-equals to assign a value.*  
    print( "Here, take mine." )     *\#The consequences of the if-condition are indented*

**else:**  
    print( "Get a dog, then." )  
    print( "Huskies are a nice breed." )  *\#An **if** or an **else** can have multiple consequences.*  
                                                                                       *Each consequence must be indented.*

*\#A more user-friendly version of the same program*  
likeCats \= input( "Do you like cats? ")

**if** likeCats **in** \["yes", "y", "Y", "Yes", "YES", "yeah", "sure"\]**:**   *\#Neat trick, eh?*  
    print( "Here, take mine." )

**else:**  
    print( "Get a dog, then." )  
    print( "Huskies are a nice breed." )

**If-elif-else statements**  
grade \= int(input( "What grade are you in?" ))

**if** grade \<= 8**:**    *\#The symbol "**\<="** means "less than or equal to".  Using just "**\<**" means "less than"*  
    print( "Hey, go back to Laurelwood\!" )

**elif** grade \== 9**:**    *\#"**elif**" is Python's way of saying "**Else If**".  The double "**\==**" means "exactly equal to"*  
    print( "Welcome to LHSS\!" )  
    print( "Here, carry my books." )  *\#An **if**, **elif** or **else** can have multiple consequences, all indented*  

**elif** grade \== 10**:**  
    print( "Have fun on the Lit Test, ha ha\!" )

**elif** grade \== 11**:**  
    print( "Two more years of this?\!" )

**elif** grade \== 12**:**  
    print( "Enjoy your last year" )  
    print( "...unless you failed English, ha ha." )

**else:**   *\#"Else" means "if none of the above conditions was true…"*  
     print( "Sorry, grades over 12 aren’t possible" )

**Other types of if-conditions besides \==, \> and \<**   
dist \= float(input( "Enter the distance you drove, in kilometers:  "))  
time \= float(input( "Enter the time it took, in hours:  "))

**if** **time \!= 0:**   *\# Meaning, **not zero**.  Exclamation mark means "not".*  
    avgSpeed \= dist/time   *\#We can safely divide by **time** because we know that **time** isn't 0*

    **if** dist \< 0 **or** dist \> 40000:  *\#Joining two conditions with an **or** tests if either one of them is true*  
print( "Get real\!  That distance isn't physically possible on planet Earth" )

    **elif** **90 \<= avgSpeed \<= 110**:    *\#Testing that a variable is within a certain range of values*  
	print( "You were going a safe speed on average." )

    **else**:  
	print( "You were a danger to other drivers\!" )

**else**:  
	print("ERROR\! DIVISION BY ZERO.")  *\#Since **time** equals zero*

**Math & rounding**  
**from** math **import** \*    *\#include this line whenever you need **sqrt**, **pi**, **sin** or **cos***

a \= 5  
b \= 6  
c \= **sqrt**( a\*\*2 \+ b\*\*2 )   *\#using Pythagorean theorem*  
print( "The hypotenuse of the right triangle with short sides", a, "and", b, "is", c )

area \= **pi**\*17\*\*2  
print( "The area of the circle with radius 17 is", area )  →  907.92027

myAverage \= (100+50)/2  
print( "The average  is", myAverage )   →  75

x \= **int**( "4" )	*\#**int**() applied to a string-number returns the actual number, which can now be used*   
print( x )  →  4                                                                                                                              *in later calculations*	  
print( x+3 )  →  7	

y \= **int**( 7.935 )	*\#**int**() applied to a decimal number returns just the integer part with the*   
                                       *decimal part dropped*		  
print( y )  →  7				  
					  
z \= **round**( 7.9356 ) 	   *\#rounding to the nearest integer*  
print( z )  →  8

w \= **round**( 7.9356, 2 )   *\#rounding to 2 decimal places*  
print( w )  →  7.94

biggerOne \= **max**( 4, 83 )   *\#Sets biggerOne to 83*  
smallerOne \= **min**( 4, 83 )   *\#Sets smallerOne to 4*

**Trig**  
**from** math **import** \*

*\#Sine and cosine*  
angleInDegrees= float(input( "Enter an angle in degrees:  "))  
angleInRadians \= **radians**( angleInDegrees )   *\#The **radians**() function converts **deg** to **rad***  
y \= 375 \* **sin**( angleInRadians )  *\#**sin**() and **cos**() calculate in radians*

*\#Inverse sine and cosine*  
theta \= **acos**(0.5000)     *\#**acos**() means cos\-1(), i.e. inverse cosine.  It returns the angle in radians*  
thetaInDegrees \= **degrees**( theta )   *\#The **degrees**() function converts **rad** to **deg***  
print( "Your angle in degrees is", thetaInDegrees) →  60.0  
print( "Your angle in degrees is", str(thetaInDegrees) \+ "\\u00b0" ) →  60.0°    *\#Even cooler\!*

print( sin(0.42)\*\*2 \+ cos(0.42)\*\*2 )  →  1   *\#since sin2 x \+ cos2 x \= 1 for all x*

**While loops**  
x \= 64			

**while** x \> 5:		64	  
    print( x )		32	  
    x \= x / 2			16  
  8  
 		              	

guess \= input( "What’s the name of our school? " )

**while** guess **not in** \["LHSS",  "Laurel Heights Secondary School"\]:  
     print( "Sorry, try again." )  
     guess \= input( "What’s the name of our school?" )

print( "You got it\!" )

**For loops**  
**for** friend **in** \[ "Maia", "Bob", "Lin" \]:	Maia is awesome\!  
    print( friend, "is awesome\!" )		Bob is awesome\!  
							Lin is awesome\!

**for** num **in range**( 6 ):				num is now 0  
    print( "num is now", num)			num is now 1  
							num is now 2  
							num is now 3  
							num is now 4  
							num is now 5

**for** x **in range**(-2, 4):				\-2	\-9   	  
    y \= 5\*x \+ 1					\-1	\-4  
    print( x, "\\t", y)				0	1													1	6  
							2	11  
							3	16

*\#Nested loop*

| for x in range( 3 ):    print( "Red fish" )    for y in range( 4 ):	           print( "Blue fish" )     print("\*\*\*\*\*\*\*\*\*") print("We're done counting fish") | Red fish Blue fish Blue fish Blue fish Blue fish \*\*\*\*\*\*\*\*\* Red fish Blue fish Blue fish Blue fish Blue fish \*\*\*\*\*\*\*\*\* Red fish Blue fish Blue fish Blue fish Blue fish \*\*\*\*\*\*\*\*\* We're done counting fish  |
| :---- | :---- |

**Generating random numbers & random choices**  
from random import \*

computerMove \= **choice**( \[ "rock", "paper", "scissors"\] )   *\#Picks a random item from a list*   
randomDieRoll \= **randint**(1, 6\)                          *\#Picks a random integer between 1 and 6*  
randomPrice \= **uniform**(200.00, 1999.99)    *\#Picks a random decimal value* 

*\#Another way to pick a random item from a list*  
gameOptions \= \[ "rock", "paper", "scissors"\]   
computerMove \= **choice**( gameOptions )

**Graphics**  
from tkinter import \*  
myWindow \= Tk()  
screen \= Canvas( myWindow, width=800, height=600, background \= "white" )  
screen.pack()

myWeddingRing \= screen.create\_oval(10, 10, 40, 59, outline="gold", **width=5**)

myLine \= screen.create\_line(0, 0, 100, 212, fill= "lawn green", width=3)  
myJaggedLine \= screen.create\_line(0, 0, 100, 212, 56, 98, 55, 10, fill="red")  
myWigglyLine \= screen.create\_line(0, 0, 100, 212, 56, 98, 55, 10, fill="red", smooth=True)

myTriangle \= screen.create\_polygon(50, 25, 175, 36, 500, 233, fill= "grey37")  
myTarSpill \= screen.create\_polygon(90, 25, 175, 36, 500, 233, fill="black", smooth=True)

myInsult \= screen.create\_text(50, 64, text="Thou cream faced loon\!", font="Arial 20")

*\#Draws grid lines, spaced 50 pixels apart.  This helps you plan your scene.*  
spacing \= 50

for x in range(0, 1000, spacing):   
    screen.create\_line( x, 25, x, 1000, fill="blue")  
    screen.create\_text( x, 5, text=str(x), font="Times 9", anchor \= N)

for y in range(0, 1000, spacing):  
    screen.create\_line( 25, y, 1000, y, fill="blue")  
    screen.create\_text( 5, y, text=str(y), font="Times 9", anchor \= W)

[A full list of named Python colours](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)

[Millions of HTML colours using hexadecimal codes](https://www.w3schools.com/colors/colors_picker.asp)

[How to run Python tkinter graphics on a Chromebook](https://docs.google.com/document/d/1Z3KEZmA7iJyHm8szQha3v6Vig7QJmDHrNCBeSRG9zEE/edit?usp=sharing)

Replit supported fonts: DejaVu Sans Mono, FreeSerif, DejaVu Sans, FreeSans, DejaVu Serif, FreeMono

**Animation**  
from tkinter import \*  
myInterface \= Tk()  
screen \= Canvas( myInterface, width=800, height=800, background \= "white" )  
screen.pack()

from time import \*  *\#Import **time** to use the **sleep**() procedure, which lets you delay between frames*

*\#Ball flying in a STRAIGHT LINE to the right at 5 pixels per frame, starting at position x \= 300*

x \= 300    *\#Initial (x, y) position and radius of the ball*   
y \= 150  
r \= 10

for f in range(100):   *\#For each frame of the animation...*   
	ball \= screen.create\_oval( x-r, y-r, x+r, y+r, fill= "blue" )   *\#Creates the ball in its current spot* 

	screen.update()		*\#Updates the screen (actually puts the created objects on screen)*  
sleep(0.03)			*\#Pauses for a short instant, so the eye has enough time to see it*   
	screen.delete( ball )	*\#Deletes the ball before creating the next frame* 

	x \= x \+ 5			*\#updates the position of the ball in preparation for the next frame*

*\#Ball flying in a PARABOLIC trajectory, with gravity strength 0.2, initial upward*     
   *speed 15,  initial height 600, horizontal speed 3 and initial x-position 50*

for f in range(100):  
	x \= 3\*f \+ 50                               *\#LINEAR motion in the horizontal direction*  
	y \= 0.2\*f\*\*2 \- 15\*f \+ 600      *\#QUADRATIC motion in the vertical direction* 

ball \= screen.create\_oval( x-r, y-r, x+r, y+r, fill= "blue" )

	screen.update()  
sleep(0.03)  
	screen.delete( ball )

**Arrays**  
**A** \= \["CS", "is", "cooler", "than", "chemistry"\]   *\#An array with 5 items, indexed 0, 1, 2, 3, 4*

print( **A**\[3\] )  →  than  
print( **A**\[0\] )  →  CS

print( **len**(**A**) )  →  5

for i in range( **len**(**A**) ):   	→ 	CS  
  	print( **A**\[i\] )				is  
						cooler  
						than  
						chemistry

*\#Determining the index of a particular value*  
x \= **A**.index( "cooler" )  →  2, *since* "cooler" *is at index 2*

*\#Adding a new value to an array*  
**A**.append("yo\!")  → *A is now* \["CS", "is", "cooler", "than", "chemistry", "yo\!"\]

*\#Removing a value from an array*  
**A**.remove( "chemistry" )  →  *A is now* \["CS", "is", "cooler", "than", "yo\!"\]  
**A**.remove( **A**\[0\] )  →  *A is now* \["is", "cooler", "than", "yo\!"\]  *\#Removing the item at index 0*

*\#Combining arrays in clever ways*  
A \= \["rock", "paper", "scissors"\]  
B \= \["H", "T"\]

C \= A \+ B     →   \["rock", "paper", "scissors", "H", "T"\]  
D \= B \* 4     →   \["H", "T", "H", "T",  "H", "T", "H", "T"\]  
E \= 2\*A \+ 3\*B →   \["rock", "paper", "scissors", "rock", "paper", "scissors", "H",  "T", "H",   
                                   "T",  "H", "T"\]

*\#Arrays can contain other arrays.  These are also called 2-D arrays*  
myPoints \= \[\[0,0\], \[-3, 5\], \[6,-8\], \[5,12\]\]   *\#Here's a 2-D array that contains 4 ordered pairs*

print( len( myPoints) ) → 4 

print( myPoints\[2\] )  →  \[6, \-8\]  
print( myPoints\[2\]\[0\] )  →  6  
print( myPoints\[2\]\[1\] )  →  \-8

for p in myPoints:					x is 0 and y is 0  
	print( "x is ", p\[0\], " and y is", p\[1\] )		x is \-3 and y is 5  
								x is 6 and y is \-8  
								x is 5 and y is 12  
	

**Grabbing parts of strings**  
favClass \= "Computer Science\!"

print( favClass\[0\] )  →  "C"  
print( favClass\[3\] )  →  "p"

print( favClass\[-1\] )  →  "\!"    *\#Negative indices count from the end of the string, starting with \-1.*  
print( favClass\[-4\] )  →  "n" 

tIndex \= favClass.**find**( "x^2" )   *\#**find**() returns the index at which a character occurs in a string.*  
print( tIndex )  → 5                  *\#Since "t" occurs at index 5*

zIndex \= favClass.**find**( "Z" )  *\#**find**() returns **\-1** if the character doesn't occur in the string*  
print( zIndex )  → \-1  

print( favClass\[9:12\] )  →  "Sci"          *\#Substring from index 9 to 11 (like range, it goes to 1 less)*  
print( favClass\[9:\] )  →  "Science\!"    *\#Everything from index 9 to the end*  
print( favClass\[:4 \] )  →  "Comp"        *\#Everything up until index 3*  
print( favClass\[-3:\] )  →  "ce\!"             *\#The last 3 characters*   
print( favClass\[:-3\] )  →  "Computer Scien"  *\#Everything up until the last 3 characters*

**Functions & procedures**

*\#Teaching Python a new procedure named printMessageManyTimes*  
def printMessageManyTimes(msg, n):   \#*← Colon here, just like in if-statements*  
      for x in range(n):    \#*The body of the procedure. This code gets run every time the procedure is called*  
            print( msg )

*\#Using the new procedure as often as we want.  These are called "procedure-calls"*  
printMessageManyTimes("Corona", 3\)  
printMessageManyTimes("Virus", 4\)  
printMessageManyTimes("6-month March break", 2\)

*\#Output of the program above.*  
Corona  
Corona  
Corona  
Virus  
Virus  
Virus  
Virus  
6-month March break   
6-month March break 

*\#Teaching Python a new function named getAverage*  
def getAverage(a, b):  
      avg \= (a+b)/2      \#*The body of the function. This code gets run every time the function is called*  
      return avg             \#*The return-statement.  This is the answer that the function returns when it is finished running*

*\#Using the new function to compute as many averages as we want.  These are called "function-calls"*  
myAvg \= getAverage(100, 90\)  \#*A function-call is usually on the RHS of an assignment statement (equals sign)*  
yourAvg \= getAverage(93, 77\)

*\#Making use of the values we just computed above*  
print("Our two averages are: ", yourAvg, "and", myAvg)  

if myAvg \> yourAvg:  
	print("Ha ha")

else:  
	print("Aw, man")

**Special string characters**  
"\\t"		Tab  
"\\n"		Extra line-break  
"\\u00b0"	Unicode character for the *degree* symbol  
"\\u03c0"	Unicode character for the *pi* symbol 

[Millions of other Unicode characters](https://unicode-table.com/en/)

z  
