#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()

x=0
y=0
for i in range(11):
    s.create_polygon(0+x,500-y,50+x,500-y,50+x,550-y,0+x,550-y, fill='white',outline="white",width=1)
    x+=50
    y+=50
s.mainloop()
