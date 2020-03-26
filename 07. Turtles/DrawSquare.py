'''
Turtle square
this program uses the turtle module to draw squares
06.10.2018 15:56
Bogdan Prădatu
'''

print("This program draws a square with the lower left corner at coordinates (x,y), of size l")

#Define new function for keyboard input
def arguments(prompt_msg):
    while True: #create loop for error check
        try:
            variable = float(input(prompt_msg)) #convert user input to float
        except(ValueError):
            #if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            #user input was valid, end
            break
    return variable

import turtle #import turtle module

#Initialize variables
x=0
y=0
l=0
n=0

#Define workspace
window = turtle.Screen()                    #setup window
window.bgcolor("midnightblue")              #setup window color
window.title("Draw Square")                 #window title
turtle.setworldcoordinates(0, 0, 500, 500)  #define workspace coordinate system
trt = turtle.Turtle()                    #create turtle

def draw_square(x,y,l):
    "draws a square with the lower left corner at (x,y), of size l"
    x = arguments("Please input x coordinate: ")
    y = arguments("Please input y coordinate: ")
    l = arguments("Please input square size l: ")
    trt.hideturtle()         #hide turtle stamp
    trt.penup()              #raises turtle pen
    trt.setposition(x,y)     #move turtle to coordinates (x,y)
    trt.pensize(3)           #define aquare line width
    trt.pendown()            #put turtle pen down on canvas
    trt.color("red")         #define square color
    trt.setheading(0)        #set turtle facing east
    for i in range(4):
        trt.forward(l)
        trt.left(90)
#Draw circle inside square
#    turtle.setx(x+l/2)
#    turtle.circle(l/2)

n = arguments("Please enter the number of squares you would like to draw: ")
def SquareNumber(n):
    "this function calls draw_square n times"
    if n > 0:
        draw_square(x,y,l)
        SquareNumber(n-1)
SquareNumber(n)

turtle.exitonclick()
