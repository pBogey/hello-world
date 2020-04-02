'''
square pattern
06.10.2018 22:45
Bogdan Prădatu
'''

import turtle

window=turtle.Screen()
window.bgcolor("midnightblue")
window.title("SquarePattern")
turtle.setworldcoordinates(0,0,500,500)
trt = turtle.Turtle()
trt.hideturtle()
trt.color("red")
trt.penup()
trt.setposition(250,250)
trt.pensize(3)
trt.pendown()
trt.speed(0)

def draw_square():
    for i in range(4):
        trt.forward(100)
        trt.left(90)

def SquarePattern():
    h = 0
    for i in range(24):
        draw_square()
        h += 15
        trt.setheading(h)

SquarePattern()

turtle.exitonclick()
