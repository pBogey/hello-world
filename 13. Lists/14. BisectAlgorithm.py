"""
Bisect Algorithm
31.07.2019
Bogdan Prădatu
"""

import random
import bisect

lst = sorted(random.sample(range(100),15))
print("lst =",lst)

target = random.randrange(0,100)
print("\ntarget:",target)
print("\n***** Bisect *****")
print("index:",bisect.bisect(lst,target))
print("***** Bisect Right*****")
print("index:",bisect.bisect_right(lst,target))
print("***** Bisect Left*****")
print("index:",bisect.bisect_left(lst,target))

print("\n***** Insort *****")
print("lst =",lst)
bisect.insort(lst,target)
print("lst =",lst)

