#Initialize Tkinter with these
from tkinter import*
from random import*

# the functions we would have to reuse


# Random color generate
# red = #ff0000
# green = #00ff00
# blue = #0000ff
# white = #ffffff
# black = #000000

# hex colors are made of RR GG BB
# each section would be from 00 -> ff
# which equals 0 -> 255

# "{:02x}"
# converts a number into hexadecimal
# examples: 255 -> ff and 0 -> 00 and 120 -> 78
# the final result would become like "#3ab7ff"

def rand_color():

    return "#{:02x}{:02x}{:02x}".format(

        randint(0, 255),  # random R red value
        randint(0, 255),  # random G green value
        randint(0, 255)   # random B blue value
    )

# Random offset 
def jitter(amount):

    return randint(-amount, amount)
    

# Colour fading, "interpolation" 
# the word means: finding values BETWEEN values
# example: black -> gray -> white

# instead of instantly jumping from one color to another which is ugly, we would instead smoothly fade between them
# https://en.wikipedia.org/wiki/Linear_interpolation

def interp(color1, color2, fade_amount):


# lstrip("#") removes the # symbol
# example:"#ff0000" -> "ff0000"
# we only need numbers
    color1 = color1.lstrip("#")
    color2 = color2.lstrip("#")

# colors are stored ff0000
# which is again earlier RR GG BB

# [0:2] we just grab the first two letter, so we would grab R
# Same would apply for the further items G with [2:4] and B with [4:6]

# int(value,16) -> hexadecimal number system
# converts hexadecimal into normal numbers

    red1 = int(color1[0:2], 16)
    green1 = int(color1[2:4], 16)
    blue1 = int(color1[4:6], 16)

    red2 = int(color2[0:2], 16)
    green2 = int(color2[2:4], 16)
    blue2 = int(color2[4:6], 16)


# fade_amount controls the blend    
# 0 = full first color
# 1 = full second color
# 0.5 = halfway blend

# Example - red1 = 255 and red2 = 0
# fade_amount = 0.5

# result -> 255 + (0 - 255) * 0.5 = 127 -> meaning halfway faded
    final_red = int(
        red1 + (red2 - red1) * fade_amount
    )

    final_green = int(
        green1 + (green2 - green1) * fade_amount
    )

    final_blue = int(
        blue1 + (blue2 - blue1) * fade_amount
    )

# now we need to convert it back for tkinter to use
# we could just returnt the value one by one but i found it easier this way 
    return f"#{final_red:02x}{final_green:02x}{final_blue:02x}"
    
    

# borders
# each one of these has a different random screen border      |
# we store all functions inside a list then randomly pick one v


# creates glowing bars along top and bottom
def border_synth(canvas):


    # random spacing between bars larger number lew bars and vice versa
    step = randint(7, 15)

    # range(start,end,step)
    # loops across screen horizontally
    for x in range(0, 800, step):

        # random bar height
        bar_height = randint(495, 60700) / 100 # 5 - 60
        color = rand_color()


        # top rectangles
        s.create_rectangle(x, 0, x + step, bar_height, fill=color, outline="")

        # bottom rectangles
        s.create_rectangle(x, 600, x + step, 600 - bar_height, fill=color, outline="")
        
        
# triangles alaong top and bottom 
def border_triangles(canvas):        
    
    # does it before hand and makes them look funky, was experimenting
    smoothness = choice([True, False])

    
    for x in range(0, 800, 20):

        triangle_height = randint(25, 220) # 10 - 50

        color = rand_color()
        # creates a triangle
        s.create_polygon(x, 0, x + 10, triangle_height, x + 20, 0, fill=color, outline="", smooth=smoothness)


        # bottom triangle
        s.create_polygon(x, 600, x + 10, 600 - triangle_height, x + 20, 600, fill=color, outline="", smooth=smoothness)


# wave border makes curvy or zigzag lines
def border_waves(canvas):


    # these lists store points
    top_points = []

    bottom_points = []
    for x in range(0, 800, 15):


# extend() would add mulitple items into list
# example: numbers = [1,2]
# numbers.extend([3,4])

# becomes -> # [1,2,3,4]
# we use extend because:
# tkinter likes points like this x1,y1,x2,y2,x3,y3
# not like [(x1,y1),(x2,y2)]
        top_points.extend([x, randint(0, 44)])


        bottom_points.extend([x, 600 - randint(0, 40)])


# the * "unpacks" the list so tkinter would recieve 1,2,3,4 
# [1,2,3,4] -> 1,2,3,4

# Top line
    s.create_line(*top_points, smooth=True, fill=rand_color(), width=randint(2,5))

# Bottom line
    s.create_line(*bottom_points, smooth=True, fill=rand_color(), width=randint(2,5))



# Bubble border 
def border_bubbles(canvas):

    for x in range(0, 800, 25):

        offset = randint(0, 2500) / 100 # 0 - 25

        color = rand_color()

        s.create_oval(x, offset, x + 16, offset + 16, fill=color, outline="")

        s.create_oval(x, 600 - offset, x + 16, 600 - offset - 16, fill=color, outline="")


# Chaos boarder spamming the shapes everywhere
# because yes
def border_chaos(canvas):
    
    looping_items = randint(90,140)
    for i in range(looping_items):
        
        x = randint(0, 800)

        y = randint(0, 600)

        size = randint(3, 15)

        color = rand_color()

        shape_type = randint(0, 2)


        # 0 = circle
        if shape_type == 0:
            s.create_oval(x, y, x + size, y + size, fill=color, outline="")

        # 1 = square
        elif shape_type == 1:
            s.create_rectangle(x, y, x + size, y + size, fill=color, outline="")

        # 2 = triangle
        else:
            smoothness = choice([True, False])
            s.create_polygon(x, y, x + size, y, x + size // 2, y - size, fill=color, outline="", smooth=smoothness)
            
    
myInterface =Tk()
s = Canvas(myInterface, width=800, height=600, background="black")
s.pack()



# random x and y position for the eye but it
# relativly stays near the right but shifts a little
eye_xposition = randint(-120,50)
eye_yposition = randint(-25,474)

eye_color = rand_color()


# functions can actually be stored inside lists
# BUT we would have to do border_synth NOT border_synth()
# because border_synth = store the function itself
# while border_synth() would run the function
border_functions = [
    border_synth,
    border_triangles,
    border_waves,
    border_bubbles,
    border_chaos
]

# pick random border
random_border = randint(0, 4)
# run selected border function, this: border_functions[#](s)
# means: run whatever function is stored at position #
border_functions[random_border](s)


# the items below are the eyeball
s.create_oval(692 + eye_xposition,12 + eye_yposition, 702 + eye_xposition, 138 + eye_yposition, fill="white",outline="")

s.create_arc(650 + eye_xposition, 20 + eye_yposition, 750 + eye_xposition, 135 + eye_yposition, fill="white", outline="white", start=-103, extent=199)



# awd outer eye points
s.create_line(658 + eye_xposition, 3.1 + eye_yposition, 665 + eye_xposition, 6 + eye_yposition, 676 + eye_xposition, 5.3 + eye_yposition, 689 + eye_xposition, 7 + eye_yposition, 700 + eye_xposition, 10 + eye_yposition, 750 + eye_xposition, 39 + eye_yposition, 772 + eye_xposition, 50 + eye_yposition, 800 + eye_xposition, 74 + eye_yposition, 834.8 + eye_xposition, 95 + eye_yposition,fill=eye_color,width=5.3,smooth=True)

# awd inner eye points
s.create_line(694 + eye_xposition, 5 + eye_yposition, 703 + eye_xposition, 50 + eye_yposition, 699 + eye_xposition, 98 + eye_yposition, 693 + eye_xposition, 129 + eye_yposition, 687 + eye_xposition, 138 + eye_yposition, 675 + eye_xposition, 128 + eye_yposition, 666.3 + eye_xposition, 100 + eye_yposition, 657 + eye_xposition, 65 + eye_yposition, 664 + eye_xposition, 27 + eye_yposition, 672 + eye_xposition, 6 + eye_yposition, fill="white", width=10, smooth=True)



# eyelashs part
# Bottom left lashes

move_x = 0
move_y = 0

for i in range(10):

    random_offset = jitter(2)

    s.create_line(674.8 + eye_xposition + move_x, 136 + eye_yposition + move_y, 662 + eye_xposition + move_x + random_offset, 150 + eye_yposition + move_y + random_offset, 657.9 + eye_xposition + move_x + random_offset, 157.5 + eye_yposition + move_y + random_offset, fill=eye_color, width=randint(80,120)/100, smooth=True)


    # move next lash slightly, also I wanted to move it by decimal so we divide by 100 
    move_x += randint(387,403) / 100 # 3.9
    move_y += 1





# Bottom right lashes
move_x = 0
move_y = 0


for i in range(44):
    random1 = jitter(3)
    random2 = jitter(4)

    s.create_line(690.8 + eye_xposition + move_x, 146 + eye_yposition + move_y, 678 + eye_xposition + move_x + random1, 160 + eye_yposition + move_y + random1 + random2, 673.9 + eye_xposition + move_x + random1 + random2, 167.5 + eye_yposition + move_y + random1, fill=eye_color, width=1, smooth=True)


    move_x += randint(310,314) / 100 # 3.12
    move_y -= 1.2 



# Upper right lashes
move_x = 0
move_y = 0


for i in range(38):


    random1 = jitter(3)
    random2 = jitter(4)


    s.create_line(807.2 + eye_xposition + move_x - random2, 82 + eye_yposition + move_y, 808 + eye_xposition + move_x, 99 + eye_yposition + move_y + random1, 794.5 + eye_xposition + move_x - random1, 84 + eye_yposition + move_y + random1, fill=eye_color, width=1, smooth=True)


    move_x -= randint(315,325) / 100 # 3.2
    move_y -= 2.19


# Upper left lashes
# [1,-1] loop would run twice
# first - direction = 1 and second - direction = -1
# this helps mirrors the lash direction
for direction in [1, -1]:

    move_x = 0
    move_y = 0


    for i in range(12):


        random_offset = jitter(11)


        s.create_line(665 + eye_xposition + move_x, 22 + eye_yposition + move_y, 650 + eye_xposition + move_x, 32 + eye_yposition + move_y, 642 + eye_xposition + move_x, 30 + eye_yposition + move_y - random_offset, fill=eye_color, width=1, smooth=True)
        move_x += direction * 1.2
        move_y -= 2.19



# Inner pupil details

s.create_oval(663 + eye_xposition, 46 + eye_yposition, 678 + eye_xposition, 100 + eye_yposition, fill=eye_color, outline="")

s.create_oval(680.1 + eye_xposition, 50 + eye_yposition, 690.1 + eye_xposition, 70 + eye_yposition, fill=eye_color, outline="")

s.create_oval(693 + eye_xposition, 52 + eye_yposition, 707.9 + eye_xposition, 72 + eye_yposition, fill=eye_color, outline="")


# Giant energy rays

# beam starting point
beam_start_x = 685 + eye_xposition

top_y = eye_yposition
bottom_y = 143 + eye_yposition


# stores all beam divider lines
# each item: (starting_y , ending_y)
ray_points = []

# top edge
ray_points.append((top_y, 0))

# middle divider
ray_points.append((

    75 + eye_yposition,
    randint(200, 380)
))


# awd
# optional extra divider
if randint(0, 2) >= 1:

    ray_points.append((

        randint(25, 55) + eye_yposition,
        randint(80, 180)
    ))


# optional lower divider
if randint(0, 2) == 2:

    ray_points.append((

        randint(95, 125) + eye_yposition,
        randint(420, 550)
    ))


# bottom edge
ray_points.append((bottom_y, 600))


# sorting the rays sort() -> organizes list items
# key -> tells python WHAT to sort by
# lambda -> from what i understand it's like a tiny throwaway function



# ray[0] -> first value inside tuple
# example -> (75,300) ray[0] = 75


# this helps sorts rays
# from ^ to V top to bottom
#
# without sorting the rays could overlap and make it look less pretty :d
ray_points.sort(

    key=lambda ray: ray[0]
)

# generating the beam
# len(ray_points) would give us the amount of items in list


# compares the current ray with next ray
for i in range(len(ray_points) - 1):


    # unpack tuple values
    # example: (75,300) -> start_y1 = 75 and end_y1 = 300
    start_y1, end_y1 = ray_points[i]

    start_y2, end_y2 = ray_points[i + 1]

    ray_color = rand_color()
    
    # more slices would make it more smoother
    slices = randint(75,120)

    for n in range(slices):


        # creates percentage values
        #
        # EXAMPLE: 0/80, 1/80, 2/80 which is need for interpolation and fading
        fade1 = n / slices

        # awd
        fade2 = (n + 1) / slices


        # beam slowly moves left
        x1 = beam_start_x - (beam_start_x * fade1)

        x2 = beam_start_x - (beam_start_x * fade2)


        # interpolate top line
        y1a = start_y1 + ((end_y1 - start_y1) * fade1)

        y1b = start_y1 + ((end_y1 - start_y1) * fade2)


        # interpolate bottom line
        y2a = start_y2 + ((end_y2 - start_y2) * fade1)

        y2b = start_y2 + ((end_y2 - start_y2) * fade2)


        # fade beam color into black
        beam_color = interp(ray_color, "#000000", fade1)


        # beam slice polygon
        s.create_polygon(x1, y1a, x2, y1b, x2, y2b, x1, y2a, fill=beam_color, outline="",smooth=False)


# random shapes in the rays
# random amount of shapes
        shape_amount = randint(0, 2)


        for shape in range(shape_amount):


            shape_x = randint(int(x2),int(x1))


            # interpolation math again
            # finds where shape should exist
            # between top and bottom beam edges
            fade = ((shape_x - x2)/(x1 - x2 + 0.001))


            top_edge_y = y1b + ((y1a - y1b) * fade)

            bottom_edge_y = y2b + ((y2a - y2b) * fade)


            # makes it so shapes from esacping their beam sections
            if bottom_edge_y - top_edge_y < 25:
                continue


            shape_y = randint(int(top_edge_y + 10), int(bottom_edge_y - 10))


            shape_size = randint(4, 7) 

            shape_color = rand_color()

            shape_type = randint(0, 2)


            # circle
            if shape_type == 0:
                s.create_oval(shape_x - shape_size, shape_y - shape_size, shape_x + shape_size, shape_y + shape_size, fill=shape_color, outline="")

            # square
            elif shape_type == 1:
                s.create_rectangle(shape_x - shape_size, shape_y - shape_size, shape_x + shape_size, shape_y + shape_size, fill=shape_color, outline="")


            # triangle
            else:
                s.create_polygon(shape_x, shape_y - shape_size, shape_x - shape_size, shape_y + shape_size, shape_x + shape_size, shape_y + shape_size, fill=shape_color, outline="", smooth=False)

random_xtext = randint(200,400)
random_ytext = randint(50,125)
text_size = randint(18,36)


# Source - https://stackoverflow.com/a/65483075
# Posted by user13007704
# Retrieved 2026-05-12, License - CC BY-SA 4.0

text_offset = randint(-200,200) / 100

text_offset = randint(-600,600) / 100 
text_bg = s.create_text(random_xtext, random_ytext, text=("You can avoid reality, but you cannot avoid the consequences of avoiding reality."), font=("Helvetica", text_size, 'bold'), fill=rand_color(), anchor = "nw", width=370)
text_fg = s.create_text(random_xtext + text_offset, random_ytext + text_offset, text=("You can avoid reality, but you cannot avoid the consequences of avoiding reality."), font=("Helvetica", text_size, 'bold'), fill=rand_color(), anchor = "nw", width=370)


s.mainloop()
