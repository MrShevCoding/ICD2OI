from tkinter import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width=800, height=600, background="#bbbbff")
s.pack()



#Ground
s.create_rectangle(0,300,800,600,fill="green")

#Road
s.create_rectangle(0,400,800,500,fill="grey20")

#10 Yellow lane stripes
#Use a for-loop to code this 



s.mainloop()
