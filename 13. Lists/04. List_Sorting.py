"""
20.12.2018 17:04
List Sorting Algorithm
Bogdan Prădatu
"""

import random
import time
import copy

print("""This program will compare the efficiency of my sorting algorithm vs
Python's implicit sorting method and function using random lists\n\n""")

# Create random list to sort
n = random.Random().randrange(1, 100)
list1 = random.Random().sample(range(0, n), n)
list2 = copy.copy(list1)
list3 = copy.copy(list1)
print("Initial List:\n", list1)


# My sorting algorithm
def list_sort(lst, reverse=False):
    """Sort given list "lst" in ascending (default)
        or descendind (reverse = True) order"""
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if reverse is False:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            elif reverse is True:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return list1


# Measure efficiency of my sorting algo
t0 = time.perf_counter()
sorted_list = list_sort(list1, reverse=False)
t1 = time.perf_counter()

print("Sorted List (my method):\n", sorted_list)
print(f"\nSorting time: {t1-t0:.5g} seconds")

# Measure efficiency of Python sorting function
t2 = time.perf_counter()
list2 = sorted(list2)
t3 = time.perf_counter()

print("\nsorted(list) Function:\n", list2)
print(f"\nSorting time: {t3-t2:.5g} seconds")

# Measure efficiency of Python sorting method
t4 = time.perf_counter()
list3.sort()
t5 = time.perf_counter()

print("\nlist.sort() Method:\n", list3)
print(f"\nSorting time: {t5-t4:.5g} seconds")
