from math import *

for x in range(127):
    t = round(x * .1, 2)
    s = round(sin(t), 4)
    print("t = ", t, "\t", "sin(t) =", s)
