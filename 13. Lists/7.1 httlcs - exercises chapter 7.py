"""
15.10.2018 23:06
How many odd numbers are in a list?
"""

import random
list1 = random.sample(range(-100, 100), random.randrange(2, 100))
print("list1= ", list1)


def count(lst):
    count = 0
    for i in lst:
        if i % 2 != 0:
            count += 1
    return count


print("\nlist1 contains", count(list1), "odd numbers and", len(list1)-count(list1), "even numbers")


def sum_even(lst):
    sum_even = 0
    for i in lst:
        if i % 2 == 0:
            sum_even += i
    return sum_even


print("The sum of even numbers is", sum_even(list1))


def sum_negative(lst):
    sum_neg = 0
    for i in lst:
        if i < 0:
            sum_neg += i
    return sum_neg


print("The sum of negative numbers is", sum_negative(list1))


def sum_elem(lst):
    sum_elem = 0
    for i in lst:
        if i % 2 == 0:
            break
        else:
            sum_elem += i
    return sum_elem


print("The sum of all elements up to the first even number is", sum_elem(list1))


def is_prime(number):
    """Check if number is prime."""
    absolute = abs(number)
    if absolute > 1:
        for i in range(2, absolute):
            if absolute % i == 0:
                print(number, "is not a prime number")
                print(i, "*", number / i, "is", number)
                return False
        else:
            print(number, "is a prime number")
            return True
    elif abs(number) == 1:
        print("1 is neither prime, nor composite")
        return None


is_prime(list1[0])
