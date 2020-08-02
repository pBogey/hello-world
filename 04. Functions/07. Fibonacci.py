"""
Fibonacci
04.10.2018 23:12
"""

# From How to think like a computer scientist
# define fibonacci function


# Define new function for keyboard input
def arguments(prompt_msg):
    while True:  # create loop for error check
        try:
            variable = float(input(prompt_msg))  # convert user input to float
        except ValueError:
            # if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            # user input was valid, end
            break
    return variable


print("This program calculates the fibonacci function from i to x")
print("Please take care that large values for x takes a lot of time to calculate")
i = arguments("Please input value of i: ")
x = arguments("Please input value of n: ")


# it seems that there are two accepted versions
# Version 1: where F(0) = 0
# Version 2: where F(0) = 1
def fibonacci(n):
    """returns nth fibonacci number"""  # docstring
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    elif n < 0:
        return ((-1)**(n+1))*fibonacci(abs(n))
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def loop():
    """calculates fibonacci numbers between given interval"""  # docstring
    n = i
    while n <= x:
        print(fibonacci(n))
        n += 1


loop()
