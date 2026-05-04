#Initialize Tkinter with these
from tkinter import*
from random import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="red")
s.pack()

flag_spacing = 0
for i in range(3):
    
    random_y = randint(50,300)
    s.create_line(125+flag_spacing,600,125+flag_spacing,random_y, fill='black',width=12)
    
    
    de=("%02x"%randint(0,255))
    re=("%02x"%randint(0,255))
    we=("%02x"%randint(0,255))
    ge="#"
    color=ge+de+re+we
    s.create_rectangle(125+flag_spacing,random_y+100, 125+flag_spacing+100,random_y,fill=color )
    
    
    flag_spacing += randint(50,250)
s.mainloop()
