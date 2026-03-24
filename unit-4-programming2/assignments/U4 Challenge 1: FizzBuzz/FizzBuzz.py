def math(x):
    for i in range(100):
        x += 1
        status = ""
        key = 0
        if x % 3 == 0 and x % 5 == 0:
            status = "FizzBuzz"
            key = 1
        elif x % 5 == 0 and key != 1:
            status = "Buzz"
        elif x % 3 == 0 and key != 1:
            status = "Fizz"
        elif status != 1:
           status = x
        print(status)
math(0)
