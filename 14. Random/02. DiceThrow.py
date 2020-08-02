"""
16.12.2018 16:45
Random number generator for dice throw
Bogdan Prădatu
"""

import random                                   # import random module


rng = random.Random()                           # create random number generator


def dice_throw():                               # function for a double dice throw
    dice1_throw = rng.randrange(1, 7)            # return integer betwen 1 and 6
    dice2_throw = rng.randrange(1, 7)
    return dice1_throw, dice2_throw


print("This program will simulate a double dice roll\n")


while True:
    print("You rolled:", dice_throw())
    play = input("Do you want to roll again? (enter 'y' or 'yes')\n").strip().lower()
    if play not in ["y", "yes", ""]:
        print("Goodbye!")
        break
