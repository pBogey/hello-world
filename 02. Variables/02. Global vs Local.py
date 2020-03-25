"""
Global vs Local Variables
23.08.2019
Bogdan Prădatu
"""

b = 6 # Global variable

def f1(a):
    print('running f1():')
    b = 2 # Local variable
    print(a)
    print(b)

def f2(a):
    print('running f2():')
    print(a)
    print(b) # access to global value

def change_global():
    global b
    b = 10

def f3(a):
    print('running f3()')
    change_global()
    print(a)
    print(b) # global value has changed

if __name__ == "__main__":
    f1(3)
    f2(3)
    f3(3)
