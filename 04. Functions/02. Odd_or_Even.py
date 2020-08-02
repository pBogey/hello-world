"""
Recursive function: Odd or Even
15.08.2018 15:38
"""

print("this program will determine if your number is odd or even")


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


x = arguments("Please input x value: ")
t = arguments("Please input timer value: ")


def even(n):
    if abs(n) == 0:
        return True
    else:
        return odd(abs(n)-1)


def odd(n):
    return not even(abs(n))


def even_or_odd(n):
    if even(n):
        return print("Your number is even")

    if odd(n):
        return print("Your number is odd")


def countdown(ts):
    if ts <= 0:
        print("Blastoff!")
    else:
        print(ts)
        countdown(ts-1)


countdown(t)    
even_or_odd(x)

# odd(3)
# return not even(3)
# return not (odd(3-1)) = #return not (odd(2))
# return not (return not even(2)
# return not (return not (odd(2-1)) = #return not (return not (odd(1))
# return not (return not (return not even(1)))
# return not (return not (return not (odd(1-1)))) = #return not (return not (return not (odd(0))))
# return not (return not (return not (return not even(0))))
# return not (return not (return not (return not True)))
# return not (return not (return not False))
# return not (return not True)
# return not False
# return True

# Simpler function
print("\n simpler function, using %:")


def even_or_odd_2(n):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


even_or_odd_2(x)
