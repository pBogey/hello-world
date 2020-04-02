"""
19.11.2018 23:07
Tuples
Bogdan Prădatu
"""

print("Tuples introduction\n")

s = ("a")
t = ("a",)

print("""s = ("a") is: """,s,"of the type:",type(s))
print("""t = ("a",) is: """,t,"of the type:",type(t))

print("\nSo, to define a one element tuple, the final comma is necessary")

print("""\nTuples are immutable, so trying to reassign an element: t[0]="b"
will result in an error:""")
print(""" Traceback (most recent call last):
  File "C:/Users/Bogey/AppData/Local/Programs/Python/Python37-32/01. Python Learning/Learning/10. Tuples/Tuples_Intro.py", line 18, in <module>
    t[0]="b"
TypeError: 'tuple' object does not support item assignment """)

print("""\nEven though tuples are immutable, we could recreate
a new tuple with the same name:""")
tuple_example = ("b","c","d","e")
print("tuple_example =",tuple_example)
tuple_example = ("a",) + tuple_example[0:] + ("f","g","h")
print("""tuple_example = ("a",) + tuple_example[0:] + ("f","g","h")""")
print("tuple_example =",tuple_example)

print("""\nPython has a very powerful tuple assignment feature that allows
a tuple of variables on the left of an assignment to be assigned values
from a tuple on the right of the assignment.""")
print("""tuple_example_2 = ("Bogdan", 28, "Python")""")
print("""(name, age, language) = tuple_example_2""")
tuple_example_2 = ("Bogdan", 28, "Python")  #tuple packing
(name, age, language) = tuple_example_2     #tuple unpacking
print("name:",name,"age:",age, "language:",language)

print("""\nOnce in a while, it is useful to swap the values of two variables.
Python provides a form of tuple assignment that solves this problem neatly:""")
a = 1
b = 2
print("a =",a,"b =",b)
(a,b) = (b,a)
print("""(a,b) = (b,a)""")
print("a =",a,"b =",b)
