from tkinter import *
from random import *
from time import *

myInterface = Tk()
s = Canvas(myInterface, width=800, height=600, background="black")
s.pack()

s.create_rectangle(0,500,800,600, fill="saddle brown")



#tree moving variable
move_tree1 = 0
move_tree2 = 0

#pumpkin anchor points
pumAncX = 200
pumAncY = 500

pumConstant = 2.4
pumSpeedY = 10
#Loop will run amount of frames times, each cycle being 1 frame of animation

amount_frames = 100
for frames in range(amount_frames): 
    #You won't need to edit any of these values. Just create and insert tree anchor points
    #tree
    tree1 = s.create_rectangle(550 + move_tree1, 320, 600 + move_tree1, 500, fill="brown")
    tree2 = s.create_oval(520 + move_tree2, 260, 630 + move_tree2, 370, fill = "green")

    #Update the anchor points so the ball's x position changes by 10 pixels for next cycle of loop
    move_tree1 -= 2.5
    move_tree2 -= 2.5



    
    #pumpkin body
    pumpkin_body = s.create_oval(pumAncX, pumAncY-50 + pumSpeedY, pumAncX+50, pumAncY + pumSpeedY, fill="orange")
    #pumpkin stem
    pumpkin_stem = s.create_rectangle(pumAncX + 19, pumAncY - 60 + pumSpeedY, pumAncX + 31, pumAncY-50 + pumSpeedY, fill="saddle brown")
    #pumpkin face
    pumpkin_face1 = s.create_oval(pumAncX + 10, pumAncY - 40 + pumSpeedY, pumAncX + 20, pumAncY - 30 + pumSpeedY, fill="yellow")
    pumpkin_face2 = s.create_oval(pumAncX + 30, pumAncY - 40 + pumSpeedY, pumAncX + 40, pumAncY - 30 + pumSpeedY, fill="yellow")
    pumpkin_face3 = s.create_arc(pumAncX + 10, pumAncY - 40 + pumSpeedY, pumAncX + 40, pumAncY - 10 + pumSpeedY, fill="yellow", start = 180, extent = 180)
    



    #Update to place the ball on the canvas
    s.update()
    #Pause Python for a short amount of time
    sleep(0.0333)


    if frames == amount_frames - 1:
        s.update()
    else:
        #Delete the ball from the canvas
        s.delete(tree1, tree2, pumpkin_body, pumpkin_stem, pumpkin_face1, pumpkin_face2, pumpkin_face3)
        
        


    if(pumAncY >= 525):
        pumSpeedY *= -1
        
     
    if(pumAncY <= 70):
        pumSpeedY = abs(pumSpeedY)
        
    pumAncY += pumSpeedY
    
    pumAncX += pumConstant
    
    
moon_offset = 400
s.create_oval(200 - moon_offset,200 - moon_offset,400 - moon_offset,400 - moon_offset,fill='white')
s.create_oval(225 - moon_offset,225 - moon_offset,325 - moon_offset,325 - moon_offset,fill='gray')
s.create_oval(300 - moon_offset,300 - moon_offset,350 - moon_offset,350 - moon_offset,fill='gray')

s.create_oval(350 - moon_offset,325 - moon_offset,376 - moon_offset,276 - moon_offset,fill='gray')



moon_offset = 400
moon_speed = 2

for i in range(amount_frames * 5):
    main_moon = s.create_oval(200 - moon_offset + moon_speed,200 - moon_offset  + moon_speed,400 - moon_offset  + moon_speed,400 - moon_offset  + moon_speed,fill='white')
    moon_crater1 = s.create_oval(225 - moon_offset  + moon_speed,225 - moon_offset  + moon_speed,325 - moon_offset  + moon_speed,325 - moon_offset  + moon_speed,fill='gray')
    moon_crater2 = s.create_oval(300 - moon_offset  + moon_speed,300 - moon_offset  + moon_speed,350 - moon_offset  + moon_speed,350 - moon_offset  + moon_speed,fill='gray')
    moon_crater3 = s.create_oval(350 - moon_offset  + moon_speed,325 - moon_offset  + moon_speed,376 - moon_offset  + moon_speed,276 - moon_offset  + moon_speed,fill='gray')


    moon_speed += 2
    
    s.update()
    sleep(0.0333)
    s.delete(main_moon, moon_crater1, moon_crater2, moon_crater3)
s.mainloop()
