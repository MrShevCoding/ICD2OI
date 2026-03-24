# Above is my approach 1 that has 16 lines of code

# def math(x):
#     for i in range(100):
#         x += 1
#         status = ""
#         key = 0
#         if x % 3 == 0 and x % 5 == 0:
#             status = "FizzBuzz"
#             key = 1
#         elif x % 5 == 0 and key != 1:
#             status = "Buzz"
#         elif x % 3 == 0 and key != 1:
#             status = "Fizz"
#         elif status != 1:
#           status = x
#         print(status)
# math(0)

# Below is approach 2 under 1 line! It's a little tricky but it's easy if you understand
for x in range(1, 101): print("Fizz"*(x%3==0) + "Buzz"*(x%5==0) or x)
# Explanation: We loop between 1 to 100 (if we did range(1,100) number 100 wouldn't be included)
# it would print Fizz IF the i%3 does equal to 0 which equals true and does print 
# same thing with applies with Buzz

# BUT the interesting thing is if both Fizz and Buzz are true like number 15 and 90
# both factories apply which means it would print Fizz + Buzz
# if non are true and nothing else, or print x


# Now if my explanation was confusing, try the following below uncomment the 
# code, do [ctrl + /] for a chunk of code, cool command

# For fizz

# x = 3
# print(x%3)
# print(x%3==0)

# # Notice how it doesn't print
# print("Fizz" * False)

# print("Fizz" * True)


# For buzz

# x = 3
# print(x%3)
# print(x%3==0)

# # Notice how it doesn't print
# print("Fizz" * False)

# print("Fizz" * True)



# Fyi, the same format:
# for x in range(1, 101):
#     Fizz_value = "Fizz"*(x%3==0)
#     Buzz_value = "Buzz"*(x%5==0)
#     print(Fizz_value + Buzz_value or x)
    
    
