"""
27.12.2018 00:19
Binary Search: function from how to think like a computer scientist 3rd edition
Bogdan Prădatu
"""

import random

n = random.Random().randrange(20, 100)
ls = sorted(random.Random().sample(range(0, n), 20))
x = random.Random().randrange(25, 75)
print("""In order for the binary search algorithm to work,
the sequence must be sorted\n""")
print("Sequence:")
print(ls)
print("Target:")
print(x, "\n")
print("ROI = region of interest")


def binary_search(lst, target):
    """Find and return the index of target in a given sequence."""
    lower_bound = 0
    upper_bound = len(lst)-1
    while True:
        if lower_bound > upper_bound:  # empty sequence
            print("Target not found")
            return None

        # Place probe in the middle of the sequence
        mid_index = (lower_bound+upper_bound)//2

        # Fetch the item at that position
        item_at_mid = lst[mid_index]

        print("ROI[{0}:{1}](size={2}), probed=’{3}’, target=’{4}’"
              .format(lower_bound, upper_bound, upper_bound-lower_bound, item_at_mid, target))
        
        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index            # Found it
        elif item_at_mid < target:
            lower_bound = mid_index + 1          # use upper half of sequence next time
        else:
            upper_bound = mid_index              # use lower half of sequence next time


print("\nThe index of target is:", binary_search(ls, x))
