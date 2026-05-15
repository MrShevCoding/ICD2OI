##########################################################
# Original Author: Anika Armitage
##########################################################
#Initializing Tkinter, the time import, and the randomizer:
from tkinter import*
from time import*
from random import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="lightskyblue")
screen.pack()

#Sun
screen.create_oval(60,40,160,140, fill = "lightgoldenrod1", outline = "")

#Cloud
screen.create_arc(100,75,325,225, fill = "white", start = 360, extent = 180, outline = "")
screen.create_arc(225,100,400,200, fill = "white", start = 360, extent = 180, outline = "")
screen.create_arc(50,125,150,175, fill = "white", start = 360, extent = 180, outline = "")

#Asphalt
screen.create_rectangle(0,435,800,600, fill = "gray25", outline = "")

#Asphalt texture
for n in range(100):
  x = randint(0,800)
  y = randint(435,600)
  s = 5
  screen.create_oval(x,y,x+s,y+s, fill = "gray35", outline = "")

#3 point line
screen.create_arc(150,185,800,700, start = 180, extent = 90, fill = "" ,outline = "goldenrod2", width = 15)
screen.create_line(157,445,467,445, fill="gray25", width = 20)
screen.create_line(470,600,470,435, fill="gray25", width = 27)

#Key
screen.create_arc(200,300,500,585, start = 180, extent = 90, fill = "" ,outline = "goldenrod2", width = 15)
screen.create_line(350,585,800,585, fill="goldenrod2", width = 15)
screen.create_line(210,445,345,445, fill="gray25", width = 20)
screen.create_line(350,585,350,435, fill="goldenrod2", width = 15)
screen.create_rectangle(725,585,800,435, fill="goldenrod2", outline = "")

#Post
screen.create_rectangle(750,475,775,150, fill = "gray50", outline = "")
screen.create_rectangle(775,150,725,175, fill = "gray50", outline = "")

#Backboard
screen.create_rectangle(715,75,725,225, fill = "white", outline = "")

#Player
hairx1 = 50
hairx2 = 100
hairy1 = 260
hairy2 = 300

headx1 = 50
headx2 = 100
heady1 = 275
heady2 = 350

neckx1 = 70
neckx2 = 80
necky1 = 325
necky2 = 365

shirtx1 = 55
shirtx2 = 95
shirty1 = 365
shirty2 = 545

pantsx1 = 55
pantsx2 = 95
pantsy1 = 450
pantsy2 = 540

shoex1 = 55
shoex2 = 105
shoey1 = 540
shoey2 = 550

armx1 = 75
armx2 = 150
army1 = 385
army2 = 325

#Basketball
x1 = 125
x2 = 200
y1 = 250
y2 = 325

Hair = screen.create_rectangle(hairx1,hairy1,hairx2,hairy2, fill = "black")
Head = screen.create_oval(headx1,heady1,headx2,heady2, fill = "burlywood2", outline = "")
Neck = screen.create_rectangle(neckx1,necky1, neckx2,necky2, fill = "burlywood2", outline = "")
Shirt = screen.create_oval(shirtx1, shirty1, shirtx2, shirty2, fill = "seagreen", outline = "")
Pants = screen.create_rectangle(pantsx1, pantsy1, pantsx2, pantsy2, fill = "black", outline = "")
Shoe = screen.create_rectangle(shoex1, shoey1, shoex2, shoey2, fill = "darkslategray", outline = "")
Arm = screen.create_line(armx1, army1, armx2, army2, fill = "burlywood2", width =10)

#Rim
screen.create_rectangle(715,175,605,185, fill = "darkorange2", outline = "")

#Net
netx1 = 605
for net in range(9):
  netx1 = netx1+10
  nety1 = 175
  netx2 = netx1 + 10
  nety2 = 250
  screen.create_line(netx1, nety1, netx2, nety2, fill = "white", width = 3)
netx1 = 715
for net in range(9):
  netx1 = netx1-10
  nety1 = 175
  netx2 = netx1 - 10
  nety2 = 250
  screen.create_line(netx1, nety1, netx2, nety2, fill = "white", width = 3)









###################################################
# CHALLENGE: Change the following animation loop so 
# our friend Steve sinks the basket in the net!
###################################################


#Animation
for frame in range(100):  

  ###Ball X and Y anchor points - change these!##
  ballX1 = 5 * frame + 120
  ballY1 = 0.028 * frame**2 - 5 * frame + 300
  ###########################################
  
  ballX2 = ballX1 + 75
  ballY2 = ballY1 + 75

  
  
  Basketball = screen.create_oval(ballX1, ballY1, ballX2, ballY2, fill = "darkorange2", outline = "")
  


  if ballX2 > 675 and ballY2 < 250:
    screen.create_text(400, 210, text = "Score!", font = "Ariel 30", fill = "gray15")

  screen.update()
  sleep(.03)
  screen.delete(Basketball)
  
screen.mainloop()
