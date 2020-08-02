"""
Turtle square spiral
06.10.2018 23:17
Bogdan Prădatu
"""

import turtle


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


def draw_square():
    t = arguments("Please input spiral angle: ")
    x = arguments("Please input angle increment: ")
    n = arguments("Please input spiral size: ")
    l = 1
    window = turtle.Screen()
    window.bgcolor("midnightblue")
    window.title("SquarePattern")
    turtle.setworldcoordinates(0, 0, 500, 500)
    trt = turtle.Turtle()
    trt.hideturtle()
    trt.color("red")
    trt.penup()
    trt.setposition(250, 250)
    trt.pensize(2)
    trt.pendown()
    trt.speed(0)
    trt.setheading(270)
    for i in range(int(n)):
        trt.forward(l)
        trt.right(t)
        t += x
        l += 2


draw_square()
turtle.exitonclick()
