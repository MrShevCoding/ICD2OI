from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width = 800, height = 600, background = "black")
s.pack()


x=0
for i in range(16):
    s.create_oval(0+x,250,50+x,350,fill='black',outline="yellow",width=4)
    x+=50



s.mainloop()
