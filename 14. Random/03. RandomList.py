"""
16.12.2018 22:31
Create random list of integers
Bogdan Prădatu - Example from How to Think Like a Computer Scientist 3rd Edition
"""

import random


def random_int_list(n, lower, upper):
    """
    Generate a list containing 'n' random ints between
    'lower' bound and 'upper' bound. Upper bound is an open bound.
    The result list cannot contain duplicates.
    """
    rand_list = []
    rng = random.Random()
    if n > upper - lower:
        return "'n' must be at least equal to the range"
    else:
        for i in range(n):
            while True:
                candidate = rng.randrange(lower, upper)
                if candidate not in rand_list:
                    break
            rand_list.append(candidate)
        return rand_list


print(random_int_list(5, 1, 10000000))
print(random_int_list(10, 0, 10))
print(random_int_list(10, 1, 6))
