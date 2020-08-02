"""
Fruitful functions
02.10.2018 18:20

"""
# Example 1: simple function

import math  # imports the built-in math functions


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


def area(radius):
    return math.pi * radius**2
    print("This code is called DeadCode and will not be executed,"
          "because it is after an return statement")


# Example 2: None
def absoluteValue(x):
    if x < 0:
        return -x
    elif x > 0:
        return x


def repeat():
    x = arguments("Please input value for x: ")
    if x != 0:
        print(absoluteValue(x))
        repeat()
    elif x == 0:
        print(absoluteValue(x))
        return


if __name__ == "__main__":
    print("Example 1")
    print("This program will compute a circle area, based on its radius")
    radius = arguments("Please input value of radius: ")
    print(area(radius))
    print("\nPress Enter to continue with example no.2")
    input()  # wait for user to press enter to go to next line
    print("Example 2: none")
    print('if there is no return statement for a certain case,\
the function returns "none"')
    print("\nThe following function will compute the absolute\
value of a given number\nTry different values for x, then try 0\n")
    
    repeat()
