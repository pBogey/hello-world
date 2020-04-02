'''
15.10.2018 23:06
How many odd numbers are in a list?
'''

import random
list1 = random.sample(range(-100,100),random.randrange(2,100))
print("list1= ", list1)

def count(l):
    count = 0
    for i in l:
        if i%2 != 0:
            count += 1
    return count

print("\nlist1 contains",count(list1),"odd numbers and", len(list1)-count(list1),"even numbers")

def sum_even(l):
    sum_even = 0
    for i in l:
        if i%2 == 0:
            sum_even += i
    return sum_even

print("The sum of even numbers is",sum_even(list1))

def sum_negative(l):
    sum_neg = 0
    for i in l:
        if i < 0:
            sum_neg += i
    return sum_neg

print("The sum of negative numbers is",sum_negative(list1))

def sum_elem(l):
    sum_elem = 0
    for i in l:
        if i%2 == 0:
            break
        else:
            sum_elem += i
    return sum_elem

print("The sum of all elements up to the first even number is", sum_elem(list1))

def is_prime(l):
    if abs(l[0]) > 1:
        for i in range(2,abs(l[0])):
            if abs(l[0])%i == 0:
                print(l[0],"is not a prime number")
                print(i,"*",l[0]/i,"is",l[0])
                break
        else:
            print(l[0], "is a prime number")
    elif abs(l[0]) == 1:
        print("1 is neither prime, nor composite")

is_prime(list1)
