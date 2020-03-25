"""
second program written
07.08.2018
Bogdan Prădatu

The following words cannot be used as variable names:
and def exec if not return assert del finally import or try
break elif for in pass while class else from is print yield
continue except global lambda raise
"""

# Variables vs strings

#define variable
a = 5.76 #assign the value 5,76 to variable a
print("Variable \na =", a)
print(type(a), '\n')

#define integer
b = int(a) #conversion of float a to integer b
print("Integer \nb =", b)
print(type(b))
print ("a+b =", a+b, '\n')

#define float
c = float(b) #conversion of integer b to float c
print("Float \nc =", c)
print(type(c))
print ("a+c =", a+c, '\n')

#define string
d = "string"
print("String: \nd =", d)
print(type(d))

print("\nconvert float to string")
try:
    d = str(c) #transform float c to string d
    print("String \nd = str(c) =", d)
    print(type(d))
    print("d+a =", d+a)
except TypeError:
    print('d+a: TypeError: can only concatenate str (not "int") to str')

