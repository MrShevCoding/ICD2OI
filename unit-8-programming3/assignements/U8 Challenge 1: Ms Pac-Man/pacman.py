#Initialize Tkinter with these
from tkinter import*
myInterface = Tk()
s = Canvas( myInterface, width=800, height=600, background="black")
s.pack()
s.create_polygon(230,235,218,198,267,165,296,200,fill='red',smooth=True)
s.create_oval(195,245,215,265,fill='red')
s.create_oval(185,235,205,255,fill='red')
s.create_polygon(266,255,218,198,186,244,226,266,fill='red',smooth=True)

s.create_arc(200,200,400,400, start=-30, extent=-300,fill='yellow')




s.create_oval(205,190,240,230, fill="red")


#Top left ribbon ends
s.create_oval(270,182,290,202, fill="red")
s.create_oval(260,165,280,185,fill="red")

#lips
s.create_polygon(375,342,352,345,352,330,fill='orange',smooth=True)
s.create_polygon(352,273,375,258,340,262,fill='orange',smooth=True)

#Eyeballs
s.create_oval(295,275,310,215,fill='black')
s.create_polygon(290,258,290,240,300,250,fill='yellow',smooth=False)


s.create_line(300,225,315,238,330,218,fill='black',width=4,smooth=True)
s.create_line(300,225,315,238,336,233,fill='black',width=4,smooth=True)

s.create_arc(297,220,307,268,start=0,extent=180,fill='orange')



s.mainloop()
