import tkinter as tk
from time import *
from math import *
from random import *


# Earlier, I was having problems with animating such a limited 
# we would have to do this evey items 
#    update the obj (x + movement or angle or special gimick, y + movement or angle or special gimick)
#    s.update()
#    t.sleep()
#    s.delete(object)


# While it would work, i'm lazy and want to do big items at the same time and overlap
# I found a different method that

# - Object movement with s.move()
# - Coordinate updates with s.coords()
# - Grouped tags for composite objects
# - Interpolation math for smooth transitions
# - Timed frame loops that control multiple things at once
#
# This instead creates smoother animation, better structure,
# and allows multiple animated systems to run together.
#
# update() and sleep() are STILL used in this project,
# but in a much more controlled and intentional way.
#
# Sources:
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/
# https://tkdocs.com/
# https://docs.python.org/3/library/tkinter.html


# Helper functions that we will use throughout


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
# we could just return the value below one by one but i found it easier this way 
    return f"#{final_red:02x}{final_green:02x}{final_blue:02x}"
    
    
    
def make_cloud(cx, cy):
    # Draws a fluffy cartoon cloud from several overlapping ovals.
    # The cloud is centred at (cx, cy). All ovals share a unique tag
    # so we can move the whole cloud as one unit later.
    # Returns the tag (ex "cloud_1234").
    tag = "cloud_" + str(randint(1000, 9999))
    num_puffs = randint(5, 8)   # how many oval puffs

    for i in range(num_puffs):
        # Scatter the puffs randomly around the centre.
        dx = randint(-35, 35)   # horizontal offset
        dy = randint(-15, 15)   # vertical offset
        w = randint(25, 55) # random width
        h = randint(18, 35) # random height
        s.create_oval(
            cx + dx - w//2, cy + dy - h//2, # top‑left
            cx + dx + w//2, cy + dy + h//2, # bottom‑right
            fill="white", outline="lightgray", tags=tag
        )
    return tag



def show_message(word):
    # Displays a huge white text with a black shadow that zooms in,
    # holds, then shrinks and disappears. The shadow (offset by 2 px)
    # makes it readable against bright backgrounds like the sky.

    # Shadow text – black, offset slightly.
    shadow = s.create_text(
        402, 302, text=word,
        font=("Arial", 1), fill="black", tags="message"
    )
    # Main text – white, exactly centred.
    msg = s.create_text(
        400, 300, text=word,
        font=("Arial", 1), fill="white", tags="message"
    )
    
    # Part 1: Zoom in
    # the font would grows rapidly from 1 to 120.
    for size in range(1, 120, 5):
        s.itemconfig(shadow, font=("Arial", size))
        s.itemconfig(msg, font=("Arial", size))
        s.update()
        sleep(0.01)

    # Hold at the largest size for impact.
    sleep(1)

    # Part 2: Shrink a bit (120 → 50) to settle.
    for size in range(120, 49, -5):
        s.itemconfig(shadow, font=("Arial", size))
        s.itemconfig(msg, font=("Arial", size))
        s.update()
        sleep(0.02)

    # Remove the message from the screen.
    s.delete(shadow, msg)

# later used for the fishing part 
def set_fish(fx, fy):
    # Move the whole fish group so its top‑left corner is at (fx, fy)
    s.coords(fish_body, fx, fy, fx+fish_w, fy+fish_h)
    s.coords(fish_tail,
                  fx+fish_w, fy+fish_h*0.2,
                  fx+fish_w+18, fy+fish_h*0.5,
                  fx+fish_w, fy+fish_h*0.8)
    s.coords(fish_eye,
                  fx+fish_w*0.15, fy+fish_h*0.25,
                  fx+fish_w*0.35, fy+fish_h*0.65)

    
    
# Setup the Tkinter s
root = tk.Tk()
s = tk.Canvas(root, width=800, height=600, background='black')
s.pack()

# The scene is built from three rectangles: sky, ocean, sand.
# Their sizes are changed later during the zoom effect.
sky = s.create_rectangle(0, 0, 800, 350, fill="#1a1a3e", outline="")
ocean = s.create_rectangle(0, 350, 800, 500, fill="#0b3b60", outline="")
sand = s.create_rectangle(0, 500, 800, 600, fill="#c2b280", outline="")

    
# The sun is a simple orange circle. Rays are lines radiating
# outward. We store (angle, canvas_id) for easy animation.
sun = s.create_oval(370, 410, 430, 470, fill="#ff4500", outline="")
rays = []
for angle in range(0, 360, 30): # one ray every 30 deg
    ray = s.create_line(400, 440, 400, 440, fill="#ff6600", width=2)
    rays.append((angle, ray))
    

# Composite objects are groups of shapes that act as one thing.
# The boat has a concave, a mast, and a triangular sail.
# They share the tag "boat" so we can move / scale them together.
#
# Instead of moving each piece one‑by‑one, we instead can
# canvas.move("boat", dx, dy)

hull_points = [0,0, 84,0, 78,20, 6,20]  # 1.2× wider than original
hull = s.create_polygon(hull_points, fill="brown", tags="boat")
mast = s.create_line(42, 0, 42, -70, fill="brown", width=4, tags="boat")

sail_color = rand_color()   # random sail colour every run
sail = s.create_polygon(
    42, -65, 78, -10, 42, -10,
    fill=sail_color, outline="black", tags="boat"
)


# Move the whole boat off‑screen left – it will come back :).
s.move("boat", -100, 420)

# Save original geometry so we can rebuild the boat during the zoom transition.
orig_hull_pts = hull_points[:]
orig_mast_dx, orig_mast_dy = 42, -70 # mast relative to hull top‑left
orig_sail_pts = [42, -65, 78, -10, 42, -10]


# The fish is made of an oval body, a triangular tail,
# and a small white eye. All pieces share the tag "fish".
fish_color = rand_color()
fish_w, fish_h = 40, 20 # body width & height

fish_body = s.create_oval(
    0, 0, fish_w, fish_h,
    fill=fish_color, outline="black", tags="fish"
)
# Tail attached to the RIGHT side -> fish faces LEFT.
fish_tail = s.create_polygon(
    fish_w, fish_h*0.2, # top‑base
    fish_w + 18, fish_h*0.5, # tip
    fish_w, fish_h*0.8, # bottom‑base
    fill=fish_color, outline="black", tags="fish"
)
# Eye near the front (left edge) of the body.
fish_eye = s.create_oval(
    fish_w*0.15, fish_h*0.25,
    fish_w*0.35, fish_h*0.65,
    fill="white", outline="black", tags="fish"
)
# Hide the fish off‑screen
s.move("fish", 1000, 1000)




# Everything below is randomly placed so the beach
# looks different every time the program runs.

# Coconut Trees (1-6)
num_trees = randint(1, 6)
leaf_colors = ["#228B22", "#2E8B57", "#006400", "#32CD32", "#008000"]

for i in range(num_trees):
    # Trunk base position – firmly on the sand.
    base_x = randint(20, 280) # stay on the left half
    base_y = randint(525, 575) # sand zone
    trunk_height = randint(80, 150)
    top_x = base_x + randint(-5, 5) # slight random lean
    top_y = base_y - trunk_height

    # Draw the trunk.
    s.create_polygon(
        base_x-8, base_y, base_x+8, base_y,
        top_x+4, top_y, top_x-4, top_y,
        fill="#8B4513", outline="#5C3317", tags="beach_item"
    )

    # Random leaves (4–12) from the trunk top.
    num_leaves = randint(4, 12)
    for i in range(num_leaves):
        leaf_base_x = top_x + randint(-8, 8)
        leaf_base_y = top_y + randint(-5, 5)

        # Each leaf is a random polygon with 3–5 points.
        num_points = randint(3, 5)
        points = [leaf_base_x, leaf_base_y] # start at base
        for j in range(num_points):
            angle = -90 + randint(-60, 60) # mostly upward
            length = randint(30, 80)
            rad = radians(angle)
            px = leaf_base_x + length * cos(rad)
            py = leaf_base_y + length * sin(rad)
            points.extend([px, py])
        points.extend([leaf_base_x, leaf_base_y]) # close shape
        color = choice(leaf_colors)
        s.create_polygon(points, fill=color, outline="#004d00", tags="beach_item")

# The little specks of sand
grains = []
grain_amount = randint(200, 1000)
for i in range(grain_amount):
    grain_size = randint(210, 350) / 100   # 2.1–3.5 pixels
    x = randint(0, 800)
    y = randint(500, 595)
    grain = s.create_oval(
        x, y, x+grain_size, y+grain_size,
        fill="#8B7355", outline="", tags="beach_item"
    )
    grains.append(grain)



num_clouds = randint(0, 12)
clouds = []  # list of (tag, horizontal_drift_speed)
for i in range(num_clouds):
    cx = randint(50, 750)
    cy = randint(40, 200)
    tag = make_cloud(cx, cy)
    # Random slow speed, left or right.
    dx = uniform(0.2, 0.8) * choice([-1, 1])
    clouds.append((tag, dx))
    
    
# Shells (0–4) with 3 possible different shapes
num_shells = randint(0, 4)
for j in range(num_shells):
    sx = randint(0, 750)
    sy = randint(515, 580)
    shell_color = rand_color()
    shell_type = randint(1, 3)

    if shell_type == 1:
        # Oval shell with ridge lines.
        s.create_oval(sx, sy, sx+20, sy+8, fill=shell_color,
                          outline="#DEB887", tags="beach_item")
        for i in range(3):
            s.create_line(sx+4 + i*6, sy+1, sx+6 + i*6, sy+7,
                              fill="#DEB887", width=1, tags="beach_item")
    elif shell_type == 2:
        # Spiral shell (simple polygon).
        s.create_polygon(sx, sy+6, sx+10, sy, sx+18, sy+2, sx+14, sy+8,
                              fill=shell_color, outline="#8B7355", tags="beach_item")
    else:
        # Clam shell (two arcs forming a circle).
        s.create_arc(sx, sy, sx+18, sy+10, start=0, extent=180,
                          style="chord", fill=shell_color, outline="#8B7355",
                          tags="beach_item")
        s.create_arc(sx, sy, sx+18, sy+10, start=0, extent=-180,
                          style="chord", fill=shell_color, outline="#8B7355",
                          tags="beach_item")   


# Some star fishes!
num_stars = randint(0, 3)
for i in range(num_stars):
    sx = randint(0, 750)
    sy = randint(515, 580)
    star_color = rand_color()
    r1, r2 = 12, 5 # outer and inner radii for a 5‑pointed star
    points = []

    for j in range(5):
        # Outer point angle
        angle_outer = radians(-90 + i * 72)
        # Jitter gives the starfish a natural, imperfect look.
        px_outer = sx + r1 * cos(angle_outer) + jitter(2)
        py_outer = sy + r1 * sin(angle_outer) + jitter(2)
        points.extend([px_outer, py_outer])

        # Inner point (halfway between outer points)
        angle_inner = angle_outer + radians(36)
        px_inner = sx + r2 * cos(angle_inner) + jitter(2)
        py_inner = sy + r2 * sin(angle_inner) + jitter(2)
        points.extend([px_inner, py_inner])

    s.create_polygon(points, fill=star_color, outline="#8B7355",
                         tags="beach_item")




# 1 lonely crab with 5 different movement patterns

crab_color = rand_color()
crab_body = s.create_oval(0, 0, 30, 20, fill=crab_color, tags="crab")

crab_legs = []
leg_coords = [
    (0, 5, -8, 12), (2, 8, -6, 16), (0, 15, -8, 22), (2, 18, -6, 26),
    (30, 5, 38, 12), (28, 8, 36, 16), (30, 15, 38, 22), (28, 18, 36, 26)
]
for x1, y1, x2, y2 in leg_coords:
    leg = s.create_line(x1, y1, x2, y2, fill=crab_color, width=2, tags="crab")
    crab_legs.append(leg)

crab_claw1 = s.create_line(0, 2, -12, -2, fill=crab_color, width=3, tags="crab")
crab_claw2 = s.create_line(30, 2, 42, -2, fill=crab_color, width=3, tags="crab")
crab_claw_tip1 = s.create_oval(-14, -6, -8, 0, fill=crab_color, tags="crab")
crab_claw_tip2 = s.create_oval(38, -6, 44, 0, fill=crab_color, tags="crab")

# Spawn the crab at a random spot on the sand.
crab_spawn_x = randint(50, 750)
crab_spawn_y = randint(510, 560)
s.move("crab", crab_spawn_x, crab_spawn_y)

# Pick a random movement pattern and set up its parameters.
crab_pattern = choice(["straight", "zigzag", "spin", "bounce", "spiral"])
crab_coords = s.coords(crab_body)
crab_cx = (crab_coords[0] + crab_coords[2]) / 2
crab_cy = (crab_coords[1] + crab_coords[3]) / 2
crab_base_x, crab_base_y = crab_cx, crab_cy
crab_speed = randint(100, 200) / 100    # 1.0–2.0

zigzag_amp, zigzag_freq = 8, 0.15
spin_radius, spin_speed_val, spin_angle = 15, 0.15, 0
bounce_dx, bounce_dy = -crab_speed, choice([-2, 2])
spiral_drift, spiral_angle, spiral_speed = crab_speed * 0.5, 0, 0.2



# The sun rises in an elliptical arc, the sky fades from night
# to day, the boat sails across the ocean on a sine wave,
# and the crab moves randomly on the beach.

night_color   = "#1a1a3e"
morning_color = "#87ceeb"

# Sun path – elliptical arc.
# The sun starts below the horizon at (400,440) and ends at the
# top‑right corner (770,30). An ellipse centre is used to create
# a smooth curved motion. (sin/cos create circular movement.)
start_x, start_y = 400, 440
end_x, end_y     = 770, 30
rx = end_x - start_x    # horizontal radius
ry = start_y - end_y    # vertical radius (positive because screen y is inverted)
cx_arc, cy_arc = start_x, end_y # ellipse centre


# Boat movement – starts off‑screen left and bobs on a sine wave.
# Sine waves naturally create smooth up‑and‑down oscillation,
# perfect for floating / bobbing motion.
boat_start_x = -100
boat_start_y = 420
boat_speed = 1.6
boat_amp = 10   # how high it bobs

total_steps = 100   # 100 frames × 0.08 s = 8 seconds
sleep_time  = 0.08

# Place the sun exactly at its starting point.
s.coords(sun, start_x-30, start_y-30, start_x+30, start_y+30)


for step in range(total_steps):
    progress = step / (total_steps - 1)   # 0 -> 1
    # angle sweeps from -90 deg (pointing down) to 0 deg (pointing right).
    angle = -pi/2 + progress * (pi/2)

    # Sun position (elliptical arc) 
    # Using cos for x and sin for y creates a quarter‑ellipse.
    # (See trigonometry unit circle: https://www.mathsisfun.com/algebra/trig-sine-cosine.html)
    current_x = cx_arc + rx * cos(angle)
    current_y = cy_arc - ry * sin(angle)   # minus because y‑axis is flipped
    s.coords(sun, current_x-30, current_y-30, current_x+30, current_y+30)
    
    
# Sky colour fade 
    new_sky = interp(night_color, morning_color, progress)
    s.itemconfig(sky, fill=new_sky)

    # Sun rays (grow + pulse) 
    # base_length increases from 20 to 70 pixels as the sun rises.
    base_length = 20 + progress * 50
    # pulse uses a fast sine wave to make the rays shimmer.
    pulse = 8 * sin(step * 0.4)
    outer_radius = base_length + pulse

    for angle_base, ray in rays:
        dx_j = jitter(3) # tiny random wobble so rays look alive
        dy_j = jitter(3)
        rad_angle = radians(angle_base)
        inner_r = 28 # inner point just outside the sun
        start_ray_x = current_x + inner_r * cos(rad_angle) + dx_j
        start_ray_y = current_y + inner_r * sin(rad_angle) + dy_j
        end_ray_x   = current_x + outer_radius * cos(rad_angle) + dx_j
        end_ray_y   = current_y + outer_radius * sin(rad_angle) + dy_j
        s.coords(ray, start_ray_x, start_ray_y, end_ray_x, end_ray_y)

    
        # Clouds drift at their own random speeds 
    for tag, dx in clouds:
        s.move(tag, dx, 0)
        coords = s.coords(tag)
        if not coords: continue # skip if cloud was already deleted
        # Find the leftmost / rightmost x of all ovals in this cloud.
        xs = [coords[i] for i in range(0, len(coords), 2)]
        min_x, max_x = min(xs), max(xs)
        width = max_x - min_x
        # Wrap around the screen when the cloud goes off‑screen.
        if dx > 0 and min_x > 800:
            s.move(tag, -(800 + width), 0)
        elif dx < 0 and max_x < 0:
            s.move(tag, 800 + width, 0)
    
      # Boat bobs on a sine wave while moving right
    # Sine waves are perfect for bobbing because they create
    # smooth, repeating up‑and‑down motion without sudden snaps
    # found it cool it's looks.
    new_boat_x = boat_start_x + step * boat_speed
    new_boat_y = boat_start_y + boat_amp * sin(step * 0.1)
    old_hull_x = s.coords(hull)[0]
    old_hull_y = s.coords(hull)[1]
    delta_x = new_boat_x - old_hull_x
    delta_y = new_boat_y - old_hull_y
    s.move("boat", delta_x, delta_y)

    
      # Crab movement (one of five random patterns) 
    if crab_pattern == "straight":
        s.move("crab", -crab_speed, 0)
        crab_cx -= crab_speed

    elif crab_pattern == "zigzag":
        new_x = crab_cx - crab_speed
        new_y = crab_base_y + zigzag_amp * sin(step * zigzag_freq)
        # Keep the crab on the sand.
        if new_y > 560: 
            new_y = 560
        if new_y < 510: 
            new_y = 510
        dx = new_x - crab_cx
        dy = new_y - crab_cy
        s.move("crab", dx, dy)
        crab_cx, crab_cy = new_x, new_y

    elif crab_pattern == "spin":
        spin_angle += spin_speed_val
        new_x = crab_base_x + spin_radius * cos(spin_angle)
        new_y = crab_base_y + spin_radius * sin(spin_angle)
        if new_y > 560: 
            new_y = 560
        if new_y < 510:
            new_y = 510
        dx = new_x - crab_cx
        dy = new_y - crab_cy
        s.move("crab", dx, dy)
        crab_cx, crab_cy = new_x, new_y

    elif crab_pattern == "bounce":
        new_x = crab_cx + bounce_dx
        new_y = crab_cy + bounce_dy
        if new_x < 30 or new_x > 770:
            bounce_dx = -bounce_dx  # reverse horizontal direction
            new_x = crab_cx + bounce_dx
        if new_y < 510 or new_y > 560:
            bounce_dy = -bounce_dy  # reverse vertical direction
            new_y = crab_cy + bounce_dy
        dx = new_x - crab_cx
        dy = new_y - crab_cy
        s.move("crab", dx, dy)
        crab_cx, crab_cy = new_x, new_y

    elif crab_pattern == "spiral":
        spiral_angle += spiral_speed
        crab_base_x -= spiral_drift
        if crab_base_x < 30: 
            crab_base_x = 770   # wrap around
        new_x = crab_base_x + spin_radius * cos(spiral_angle)
        new_y = crab_base_y + spin_radius * sin(spiral_angle)
        if new_y > 560: 
            new_y = 560
        if new_y < 510: 
            new_y = 510
        dx = new_x - crab_cx
        dy = new_y - crab_cy
        s.move("crab", dx, dy)
        crab_cx, crab_cy = new_x, new_y
        
        
    s.update()
    sleep(sleep_time)
    
    
# The beach is cleared, the ocean floods the sand, the boat
# zooms to the centre and doubles in size, a stickman appears,
# and he casts a fishing line with a two‑arm overhead throw.

# Remove everything that belongs to the beach scene.
s.delete("beach_item") # trees, shells, starfish, grains
s.delete("crab") # crab



# Push the sand behind the ocean – the ocean will expand and cover it.
s.tag_lower(sand, ocean)

# Smooth zoom‑in: ocean expands downward, boat moves to centre and doubles
zoom_max = 160 # pixels the ocean's bottom edge will move down
steps_zoom = 40
zoom_per_step = zoom_max / steps_zoom

target_center_x = 400  # where the boat will end up (canvas centre)
target_center_y = 420

# Find the boat's current centre (from previous).
hull_coords = s.coords(hull)
start_hull_cx = (hull_coords[0] + hull_coords[2]) / 2
start_hull_cy = (hull_coords[1] + hull_coords[3]) / 2

for i in range(steps_zoom):
    t = (i + 1) / steps_zoom # 0 -> 1

    # Expand ocean downward to cover the sand.
    new_ocean_bottom = 500 + zoom_per_step * (i+1)
    s.coords(ocean, 0, 350, 800, new_ocean_bottom)

    # Move boat toward the target and scale it up.
    new_cx = start_hull_cx + (target_center_x - start_hull_cx) * t
    new_cy = start_hull_cy + (target_center_y - start_hull_cy) * t
    cur_scale = 1 + (2 - 1) * t # grows from 1x to 2x

    # Rebuild hull polygon using original points, new centre, and new scale.
    scaled_hull = []
    for j in range(0, len(orig_hull_pts), 2):
        px = orig_hull_pts[j] * cur_scale + new_cx - 42*cur_scale
        py = orig_hull_pts[j+1] * cur_scale + new_cy - 10*cur_scale
        scaled_hull.extend([px, py])
    s.coords(hull, *scaled_hull)

    # Mast
    mast_top_y = new_cy + orig_mast_dy * cur_scale
    s.coords(mast, new_cx, new_cy, new_cx, mast_top_y)

    # Sail
    scaled_sail = []
    for j in range(0, len(orig_sail_pts), 2):
        px = orig_sail_pts[j] * cur_scale + new_cx - 42*cur_scale
        py = orig_sail_pts[j+1] * cur_scale + new_cy
        scaled_sail.extend([px, py])
    s.coords(sail, *scaled_sail)

    s.update()
    sleep(0.02)

    
# Make sure the boat is drawn on top of the expanded ocean.
s.tag_raise("boat")
    
# Build the stickman fisherman 
# He stands directly on the hull's top edge.
hull_top_y = target_center_y - 20 # hull top at scale 2
feet_y = hull_top_y
leg_top_y = feet_y - 30
body_bottom_y = leg_top_y
body_top_y = body_bottom_y - 25
arm_y = body_bottom_y - 10 # shoulder height
neck_y = body_top_y
head_center_y = neck_y - 12


head = s.create_oval(
    target_center_x-10, head_center_y-10,
    target_center_x+10, head_center_y+10,
    fill="white", outline="black", tags="fisherman"
)
body = s.create_line(
    target_center_x, neck_y, target_center_x, body_bottom_y,
    fill="black", width=2, tags="fisherman"
)
leg_left = s.create_line(
    target_center_x, body_bottom_y, target_center_x-10, feet_y,
    fill="black", width=2, tags="fisherman"
)
leg_right = s.create_line(
    target_center_x, body_bottom_y, target_center_x+10, feet_y,
    fill="black", width=2, tags="fisherman"
)

# Two‑arm overhead casting animation
shoulder_x, shoulder_y = target_center_x, arm_y
hand_start_x, hand_start_y = target_center_x, head_center_y - 15   # hands above head

rod_length = 55
# Rod starts pointing up‑left.
init_dir_x, init_dir_y = -0.7, -0.7
mag = sqrt(init_dir_x**2 + init_dir_y**2)
init_dir_x /= mag
init_dir_y /= mag

# Rod finishes pointing right‑and‑down.
final_dir_x, final_dir_y = 0.9, 0.3
mag = sqrt(final_dir_x**2 + final_dir_y**2)
final_dir_x /= mag
final_dir_y /= mag

# Both arms start at the same position (hands together above head).
arm_left = s.create_line(
    shoulder_x, shoulder_y, hand_start_x, hand_start_y,
    fill="black", width=2, tags="fisherman"
)
arm_right = s.create_line(
    shoulder_x, shoulder_y, hand_start_x, hand_start_y,
    fill="black", width=2, tags="fisherman"
)


# Rod
rod_tip_x = hand_start_x + init_dir_x * rod_length
rod_tip_y = hand_start_y + init_dir_y * rod_length
rod = s.create_line(
    hand_start_x, hand_start_y, rod_tip_x, rod_tip_y,
    fill="brown", width=3, tags="fisherman"
)
hook = s.create_oval(
    rod_tip_x-3, rod_tip_y-3, rod_tip_x+3, rod_tip_y+3,
    fill="red", tags="fisherman"
)
# Fishing line – hidden until the hook is released.
fishing_line = s.create_line(0,0,0,0, fill="black", width=1, tags="fisherman")
s.itemconfig(fishing_line, state="hidden")


s.tag_raise("fisherman") # keep always fisherman on top
s.update()
sleep(0.5)
    
    
# Phase 1: Swing the rod forward (hands move right + down).
swing_frames = 20
for i in range(swing_frames):
    t = (i + 1) / swing_frames
    hand_x = hand_start_x + (target_center_x + 35 - hand_start_x) * t
    hand_y = hand_start_y + (arm_y - 5 - hand_start_y) * t

    # Interpolate the rod direction.
    cur_dir_x = init_dir_x + (final_dir_x - init_dir_x) * t
    cur_dir_y = init_dir_y + (final_dir_y - init_dir_y) * t
    mag = sqrt(cur_dir_x**2 + cur_dir_y**2)
    cur_dir_x /= mag
    cur_dir_y /= mag

    rod_tip_x = hand_x + cur_dir_x * rod_length
    rod_tip_y = hand_y + cur_dir_y * rod_length

    s.coords(arm_left, shoulder_x, shoulder_y, hand_x, hand_y)
    s.coords(arm_right, shoulder_x, shoulder_y, hand_x, hand_y)
    s.coords(rod, hand_x, hand_y, rod_tip_x, rod_tip_y)
    s.coords(hook, rod_tip_x-3, rod_tip_y-3, rod_tip_x+3, rod_tip_y+3)
    s.update()
    sleep(0.02)
    
    
# Remember the exact moment the hook leaves the rod.
release_hand_x, release_hand_y = hand_x, hand_y
release_rod_tip_x, release_rod_tip_y = rod_tip_x, rod_tip_y

# Where the hook should land in the water.
water_target_x = target_center_x + 140
water_target_y = 480

# Rod follow‑through – keeps moving a little after release.
follow_hand_x = target_center_x + 60
follow_hand_y = arm_y
follow_dir_x, follow_dir_y = 0.98, 0.2
mag = sqrt(follow_dir_x**2 + follow_dir_y**2)
follow_dir_x /= mag
follow_dir_y /= mag

# Parabola for the hook's flight.
# A quadratic formula (y = a*(x - h)**2 + k) creates an arc.
# The peak is halfway between start and target.
peak_x = (release_rod_tip_x + water_target_x) / 2
peak_y = release_rod_tip_y - 80
a_cast = (release_rod_tip_y - peak_y) / ((release_rod_tip_x - peak_x)**2)

s.itemconfig(fishing_line, state="normal")# show the line
    
    
flight_frames = 30
for i in range(flight_frames):
    t = (i + 1) / flight_frames
    # Rod follow‑through.
    hand_x = release_hand_x + (follow_hand_x - release_hand_x) * t
    hand_y = release_hand_y + (follow_hand_y - release_hand_y) * t
    rod_tip_x = hand_x + follow_dir_x * rod_length
    rod_tip_y = hand_y + follow_dir_y * rod_length
    # Hook flies along the parabola.
    hook_x = release_rod_tip_x + (water_target_x - release_rod_tip_x) * t
    hook_y = a_cast * (hook_x - peak_x)**2 + peak_y

    s.coords(arm_left, shoulder_x, shoulder_y, hand_x, hand_y)
    s.coords(arm_right, shoulder_x, shoulder_y, hand_x, hand_y)
    s.coords(rod, hand_x, hand_y, rod_tip_x, rod_tip_y)
    s.coords(fishing_line, rod_tip_x, rod_tip_y, hook_x, hook_y)
    s.coords(hook, hook_x-3, hook_y-3, hook_x+3, hook_y+3)
    s.update()
    sleep(0.04) 
    
    
# Final resting position of the hook in the water.
s.coords(hook, water_target_x-3, water_target_y-3, water_target_x+3, water_target_y+3)
s.coords(fishing_line, rod_tip_x, rod_tip_y, water_target_x, water_target_y)
s.update()
sleep(0.5)
    
    
# Time to do the fisherman getting (or not) the fishy

# The fish either bites and is pulled onto the boat, or escapes.
# A zooming text message announces the result.

success_words = ["Success!", "Gotcha!", "Yes!", "Alright!", "Nice!", "Perfect!", "Caught it!"]
failure_words = ["Missed!", "Nooo!", "Almost!", "Dang!", "Escaped!", "So close!"]

outcome = choice(["success", "fail"])


if outcome == "success":
    # The fisherman caught the fish!
    # Place the fish to the right of the hook.
    fish_start_x = water_target_x + 80
    fish_start_y = water_target_y - fish_h//2
    set_fish(fish_start_x, fish_start_y)
    s.addtag_withtag("fish", fish_body)
    s.addtag_withtag("fish", fish_tail)
    s.addtag_withtag("fish", fish_eye)

    # Swim toward the hook with a wavy motion.
    swim_steps = 40
    for i in range(swim_steps):
        t = (i + 1) / swim_steps
        new_x = fish_start_x - t * 80
        new_y = fish_start_y + 8 * sin(t * 3 * pi) # wavy vertical movement
        old_body_x = s.coords(fish_body)[0]
        old_body_y = s.coords(fish_body)[1]
        dx = new_x - old_body_x
        dy = new_y - old_body_y
        s.move("fish", dx, dy)
        s.update()
        sleep(0.03)
    
    
    # Bite! Attach the fish to the hook.
    set_fish(water_target_x - fish_w//2, water_target_y - fish_h//2)
    mouth_x = water_target_x - fish_w//2 # left edge = mouth
    mouth_y = water_target_y
    s.coords(hook, mouth_x-3, mouth_y-3, mouth_x+3, mouth_y+3)
    s.coords(fishing_line, rod_tip_x, rod_tip_y, mouth_x, mouth_y)
    s.update()
    sleep(0.8)
    
    
     # Pull the fish over the fisherman's head onto the deck (behind him).
    deck_x = target_center_x - 60 # left of the stickman = behind
    deck_y = hull_top_y + 5 # on the deck
    peak_y_pull = head_center_y - 60 # highest point of the arc
    cur_hand_x, cur_hand_y = hand_x, hand_y # current hand position
    
    
    pull_frames = 30
    for i in range(pull_frames):
        t = (i + 1) / pull_frames
        cur_fish_x = water_target_x + t * (deck_x - water_target_x)

        # Arc formula that guarantees the fish lands exactly on deck_y.
        mid_y = (water_target_y + deck_y) / 2
        arc_height = peak_y_pull - mid_y
        cur_fish_y = water_target_y + (deck_y - water_target_y)*t + arc_height * 4 * t * (1 - t)
    
    
        # Move the fish group.
        old_body_x = s.coords(fish_body)[0]
        old_body_y = s.coords(fish_body)[1]
        dx = cur_fish_x - old_body_x
        dy = cur_fish_y - old_body_y
        s.move("fish", dx, dy)

        # Keep the hook at the fish's mouth.
        mouth_x = cur_fish_x
        mouth_y = cur_fish_y + fish_h//2
        s.coords(hook, mouth_x-3, mouth_y-3, mouth_x+3, mouth_y+3)

        # Fisherman raises his arms to pull.
        hand_x = cur_hand_x + t * (target_center_x - cur_hand_x)
        hand_y = cur_hand_y + t * (head_center_y - 40 - cur_hand_y)
        s.coords(arm_left, shoulder_x, shoulder_y, hand_x, hand_y)
        s.coords(arm_right, shoulder_x, shoulder_y, hand_x, hand_y)
        rod_tip_x = hand_x + follow_dir_x * rod_length
        rod_tip_y = hand_y + follow_dir_y * rod_length
        s.coords(rod, hand_x, hand_y, rod_tip_x, rod_tip_y)
        s.coords(fishing_line, rod_tip_x, rod_tip_y, mouth_x, mouth_y)
        s.update()
        sleep(0.04)
    
    # Final placement on deck.
    set_fish(deck_x, deck_y)
    mouth_x = deck_x
    mouth_y = deck_y + fish_h//2
    s.coords(hook, mouth_x-3, mouth_y-3, mouth_x+3, mouth_y+3)
    s.coords(fishing_line, rod_tip_x, rod_tip_y, mouth_x, mouth_y)
    s.tag_raise("fish") # fish visible above the boat
    s.tag_raise("fisherman")
    s.update()
    show_message(choice(success_words))

    
# Or... the fisherman fails.. :(
else:
    fish_start_x = water_target_x + 80
    fish_start_y = water_target_y - fish_h//2
    set_fish(fish_start_x, fish_start_y)
    s.addtag_withtag("fish", fish_body)
    s.addtag_withtag("fish", fish_tail)
    s.addtag_withtag("fish", fish_eye)


    # Swim toward the hook (slightly slower approach).
    swim_steps = 40
    for i in range(swim_steps):
        t = (i + 1) / swim_steps
        new_x = fish_start_x - t * 70
        new_y = fish_start_y + 6 * sin(t * 3 * pi)
        old_body_x = s.coords(fish_body)[0]
        old_body_y = s.coords(fish_body)[1]
        dx = new_x - old_body_x
        dy = new_y - old_body_y
        s.move("fish", dx, dy)
        s.update()
        sleep(0.03)
    
    # Fish near the hook.
    set_fish(water_target_x - fish_w//2, water_target_y - fish_h//2)
    s.update()
    sleep(0.5)

    # Dart away at high speed in a random direction, staying in the water.
    escape_angle = uniform(pi/4, 3*pi/4) # 45deg–135deg, mostly leftwards
    escape_speed = 8.0
    dx_esc = escape_speed * cos(escape_angle)
    dy_esc = escape_speed * sin(escape_angle) - 2 # slight upward

    escape_frames = 25
    for i in range(escape_frames):
        s.move("fish", dx_esc, dy_esc)
        s.update()
        sleep(0.02)

    show_message(choice(failure_words))


# Keep the Tkinter window open.
s.mainloop()

# This project was a doozy, so here were some of the links
# i used to help me out, i would reccomand anyone new to this
# to look at the links below and compare above to see what i 
# changed slightly (still using the core concepts) to make these effects

# Tkinter Canvas Documentation:
# https://docs.python.org/3/library/tkinter.html

# TkDocs Tkinter Guide:
# https://tkdocs.com/

# Tkinter Canvas Reference:
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/

# Linear Interpolation Explanation:
# https://en.wikipedia.org/wiki/Linear_interpolation

# RGB and Hexadecimal Colors:
# https://www.w3schools.com/colors/colors_hexadecimal.asp

# Polygon and Coordinate Systems:
# https://tkdocs.com/tutorial/canvas.html

# Random Module Documentation:
# https://docs.python.org/3/library/random.html

# Math Module Documentation:
# https://docs.python.org/3/library/math.html
