'''
18.10.2018 17:34
Reverse list elements order
'''

import random
#list1 = [0,1]
list1 = random.sample(range(0,100),random.randrange(2,20))

def rev():
    for i in range(0,len(list1)//2):
        x = list1[i]
        list1[i] = (list1[len(list1)-1-i])
        list1[len(list1)-1-i] = x
    return list1

print(list1)
print(rev())
