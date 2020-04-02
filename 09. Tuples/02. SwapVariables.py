"""
16.12.2018 14:58
Value Swap
Bogdan Prădatu
"""

def swap(x,y):
    print("before swap statement: x:",x,"y:",y)
    (x,y) = (y,x)
    print("after swap statement: x:",x,"y:",y)
    return x,y

a = 5
b = 10
print("before swap function call: a:", a, "b:", b)
a,b = swap(a, b)
print("after swap function call: a:", a, "b:", b)
print("swap(a,b) =",swap(a,b))
