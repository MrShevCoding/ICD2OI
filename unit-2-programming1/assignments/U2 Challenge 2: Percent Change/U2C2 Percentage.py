import math

numb1 = int(input()) # this is the 100 perc
numb2 = int(input()) # this is the change

perc_change = abs(((numb2 - numb1) / abs(numb1)) *100)

addon = ""
if perc_change < 99:
    addon = "% decrease"
elif perc_change > 100:
    addon = "% increase"
else:
    addon = " no changes"

    

print(f"{perc_change}{addon}")
