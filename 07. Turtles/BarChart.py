'''
Bar chart
07.10.2018 13:57
Bogdan Prădatu
example from How to think like a computer scientist v3
'''

import turtle                               #import turtle module
import random                               #import random number generator
window = turtle.Screen()                    #create screen
window.bgcolor("honeydew")                  #define screen color
window.title("Bar Chart")                   #set window title
turtle.screensize(500,500)                  #set window size
tortoise = turtle.Turtle()                  #create turtle
tortoise.hideturtle()                       #hide turtle stamp
tortoise.penup()                            #raise turtle pen
tortoise.setposition(-450,0)                #position turtle
tortoise.pendown()                          #put turtle pen down
tortoise.speed(5)                           #set drawing speed

#list1 = [48, 117, 200, -50, -138, 85, 160, 260, 220, 50]  #creaste chart values
list1 = random.sample(range(-350,350),20)
def draw_bar_chart(t,h):                    #create function to draw chart
    """draw a bar chart, based on given data."""
    if abs(h) < 100:
        tortoise.color("SeaGreen","ForestGreen")    #set turtle color
    elif abs(h) >= 100 and abs(h) < 200:
        tortoise.color("orange","gold")    #set turtle color
    else:
        tortoise.color("coral3","IndianRed")             #set turtle color
    
    t.begin_fill()
    t.left(90)
    t.forward(h)
    t.right(90)
    t.forward(10)
    if h >= 0:
        t.write(h)
    else:
        t.penup()
        t.right(90)
        t.forward(15)
        t.write(h)
        t.forward(-15)
        t.left(90)
        t.pendown()
    t.forward(30)
    t.right(90)
    t.forward(h)
    t.left(90)
    t.penup()
    t.forward(5)
    t.pendown()
    t.end_fill()

for value in list1:
    draw_bar_chart(tortoise,value)

turtle.exitonclick()
