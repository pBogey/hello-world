"""
16.12.2018 16:45
Random number generator for dice throw - unfinished.
Bogdan Prădatu
"""

import random                                   # import random module
import turtle


rng = random.Random()                           # create random number generator


def dice_throw():                               # function for a double dice throw
    dice1_throw = rng.randrange(1, 7)           # return integer betwen 1 and 6
    dice2_throw = rng.randrange(1, 7)
    return dice1_throw, dice2_throw


def game():
    while True:
        print("You rolled:", dice_throw())
        play = input("""Do you want to roll again?
                        (enter 'y' or 'yes')\n""").strip().lower()
        if play not in ["y", "yes", ""]:
            print("Goodbye!")
            break


turtle.setup(500, 500)                          # Window size
window = turtle.Screen()                        # create window
window.bgcolor("peru")                          # window background color
window.title("Dice Game")                       # set window title


def dice_1():
    dice1 = turtle.Turtle()
    dice1.hideturtle()
    dice1.pensize(2)
    dice1.speed(0)
    dice1.color("black", "white")
    dice1.penup()
    dice1.goto(-200, -75)
    dice1.pendown()
    dice1.begin_fill()
    for i in range(4):
        dice1.forward(150)
        dice1.left(90)
    dice1.end_fill()
    dice1.penup()


def dice_2():
    dice2 = turtle.Turtle()
    dice2.hideturtle()
    dice2.pensize(2)
    dice2.speed(0)
    dice2.color("black", "white")
    dice2.penup()
    dice2.goto(50, -75)
    dice2.pendown()
    dice2.begin_fill()
    for i in range(4):
        dice2.forward(150)
        dice2.left(90)
    dice2.end_fill()
    dice2.penup()


def play_button():
    button = turtle.Turtle()
    button.hideturtle()
    button.pensize(2)
    button.speed(0)
    button.color("black", "blue violet")
    button.penup()
    button.goto(-75, -200)
    button.pendown()
    button.begin_fill()
    for i in range(2):
        button.forward(150)
        button.left(90)
        button.forward(50)
        button.left(90)
    button.end_fill()
    button.penup()
    button.goto(-20, -185)
    button.color("Yellow")
    button.write("Roll", font=("Monospace", 16, "bold"))


def play_button_click(x, y):
    if -75 < x < 75 and -200 < y < -150:
        game()


dice_1(), dice_2(), play_button()
window.onscreenclick(play_button_click)
window.listen()
window.mainloop()
