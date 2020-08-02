"""
String Interning
30.07.2019
Bogdan Prădatu
"""

# When Python is instructed to instantiate a new immutable object,
# it first checks to see if an identical object already exists as
# a shared object.

# CPython loads the Latin-1 range of characters unicode decimals 0
# to 255, inclusive, as shared objects every time Python is initialized.

# String interning is the method of caching particular strings in
# memory as they are instantiated. 

a = "string"
b = "string"
c = "str"+"ing"
d = "str"
e = "ing"
f = c+d
g = "".join(["s", "t", "r", "i", "n", "g"])

print("a is b:", a is b)
print("a is c:", a is c)
print("a is f:", a is f)
print("a is g:", a is g)
