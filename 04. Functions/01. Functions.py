'''
Functions
09.08.2018 20:25

Introduction to predefined python functions
'''

#Type
print("*****      Variable type     *****")
a = 1
print("a =",a)
print("type(a):",type(a))
message = "Hello, World!"
print("\nmessage =",message)
print("type(message):",type(message))

#Namespace
print("\n*****     Namespace     *****")
x = 0
print("def func1():\nx = 1\nprint('x inside func1:',x)\n")
def func1():
    x = 1
    print("x inside func1:",x,"; id(x):",id(x))
func1()
print("x in main program:",x,"; id(x):",id(x))
print("x from func1 and x from main are in different 'Namespaces'")

#Math module functions
print("\n*****     Math functions     *****")
import math #import functions of math module
print("import math")
angle = 90 # set angle value to 90 degrees
print("angle =",angle)
#function argument is in radians, so we need to convert the degrees
print("math.sin(angle*math.pi/180):",math.sin(angle*math.pi/180))

print("\nmath.sqrt(9) =",math.sqrt(9))

#lambda
print("\n*****     Lambda Function     *****\n")
l = (lambda x: x*(x+1)) (5) #(5) assigns 5 to x. could have been put in the print command, for exmaple: print((l)(5))
print("l = (lambda x: x*(x+1) (5)","\nl =",l)

#Recursive function
#example: factorial
print("\n*****     Recursive function example: factorial     *****\n")
print("x = 5", "\nfactorial 5 = 5! = 5*4*3*2*1")
def factorial(n):   #define function
    """ return n! """
    return 1 if n < 2 else n*factorial(n-1)
    #if n == 1:      #set the "base case", in order to not have an infinite function
    #    return 1
    #else:
    #    return n*factorial(n-1)
#5*factorial(4) = 5*4*factorial(3)=5*4*3*factorial(2)=5*4*3*2*factorial(1)
    
print("5! =",factorial(5))
# In Python, everything is an object (even a function)
# Functions are considered "first-class objects"
# A first class object is defined as something that can be:
## created ar runtine
## assigned to a variable or element in a data structure
## passed as an argument to a function
## returned as the result of a function
print("\n*****     First-Class Objects     *****\n")
print("type(factorial):",type(factorial))
print("factorial.__doc__:",factorial.__doc__)

print("\n*****     Higher-Order Functions     *****\n")
# Map - higher-order function (can take a function as an argument)
print("map(facotrial,range(5)):",list(map(factorial,range(5))))

