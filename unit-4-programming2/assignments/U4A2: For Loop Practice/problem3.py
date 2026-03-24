# Write a for-loop that prints a table of values for the linear 
# function y = -3x + 20 from x= -5 up to x = 5. 

print("function: function y = -3x + 20")
print("y values | x values")
print("")
# Treat i as x
for i in range(-5, 6):
    y = -3*i + 20
    
    print(f"{y} | {i}")
    print("")
