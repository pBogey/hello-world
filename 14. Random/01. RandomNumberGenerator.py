"""
16.12.2018 16:45
Random number generator intro
Bogdan Prădatu
"""

import random                                   # import random module


rng = random.Random()                           # create random number generator


def dice_throw():
    dice1_throw = rng.randrange(1, 7)            # return integer between 1 and 6
    dice2_throw = rng.randrange(1, 7)
    return dice1_throw, dice2_throw


print("dice_throw =", dice_throw())              # print two dice throw
print("dice_throw =", dice_throw())
print("dice_throw =", dice_throw())
print("dice_throw =", dice_throw())
