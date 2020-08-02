"""Event-driven programming: automatic events
20.11.2018 14:01
Bogdan Prădatu: Example from How to Think Like a Computer Scientist 3rd Edition
"""

import turtle


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)


def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 600)  # create infinite loop


# wn.ontimer(h1, 2000) #timer set and activated just once
h1()
    
wn.mainloop()
