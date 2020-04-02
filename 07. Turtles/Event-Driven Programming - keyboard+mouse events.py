"""
Event-driven programming: keyboard events

Example from How to Think Like a Computer Scientist 3rd Edition

20.11.2018 12:30
Bogdan Prădatu: modified
"""

import turtle
from tkinter import *
from tkinter import messagebox

turtle.setup(800,800) # Determine the window size
turtle.delay(1000/60)  
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling keypresses!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color
#Show help info
helper = turtle.Turtle()
helper.hideturtle()
helper.speed(0)
helper.penup()
helper.goto(-390,370)
helper.color("red")
helper.write("press F1 for help",font=("Monospace", 12, "normal"))

tess = turtle.Turtle() # Create our favorite turtle
tess.shape("turtle")
tess.shapesize(2)
tess.speed(0)
tess.color("CadetBlue")


linewidth = 1
clr_index = 0
# The next four functions are our "event handlers".
def clear():
    tess.clear()                #Clear everything tess has drawn

def fwd():
    tess.forward(30)

def rccw():
    tess.left(45)

def rcw():
    tess.right(45)

def bwd():
    tess.forward(-30)

def qt():
    wn.bye()                    # Close down the turtle window

def clr_red():
    tess.color("red")
def clr_green():
    tess.color("green")
def clr_blue():
    tess.color("blue")
def line_plus():
    global linewidth            #do no create local variable, instead use global
    if linewidth >= 20:
        linewidth = 20
    else:
        tess.pensize(linewidth+1)
        linewidth += 1
def line_minus():
    global linewidth
    if linewidth <= 1:
        linewidth = 1
    else:
        tess.pensize(linewidth-1)
        linewidth -= 1

def pen_vis():
    if tess.isdown() == True:
        tess.penup()
    else:
        tess.pendown()
def onclick_shape(x,y):
    tess.shape("circle")
    tess.shapesize(1)
    tess.pensize(5)
    #tess.color("coral")
    tess.pendown()
    tess.speed('fastest')
def drag(x,y):
    tess.ondrag(None)   #Disable event handler to avoid recursion
    tess.setheading(tess.towards(x, y))
    tess.goto(x,y)
    tess.ondrag(drag)
    
def release(x,y):
    tess.shape("turtle")
    tess.shapesize(2)
    tess.pensize(linewidth)
    tess.color("CadetBlue")

def clrs():
    global clr_index
    clrs = ["azure", "BlanchedAlmond", "burlywood","chartreuse", "cornsilk",
            "DodgerBlue", "firebrick", "honeydew", "IndianRed", "lavender",
            "LightGoldenrod", "LightSkyBlue", "maroon", "orange", "lightgreen"]
    wn.bgcolor(clrs[clr_index])
    clr_index += 1
    if clr_index >= len(clrs):
        clr_index = 0

def hlp():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()           #remove tkinter main window
    messagebox.showinfo('Information', """Up Arrow: moves turtle up by 30 units
\nLeft Arrow: rotates turtle counter-clocwise by 45 degrees
\nRight Arrow: rotates turtle clockwise by 45 degrees
\nDown Arrow: moves turtle backwards by 30 units
\nEscape: Quit
\nr: Turns turtle red
\ng: Turns turtle green
\nb: Turns turtle blue
\n+: Increase pensize
\n-: Decrease pensize
\np: Hide/show pen)
\nc: Clear window)
\nTab: Toggle background color
\nDrag With Mouse to Draw""")
    window.deiconify()
    window.destroy()
    window.quit()
    #For info on messagebox
    """http://interactivepython.org/runestone/static/CS152f17/
GUIandEventDrivenProgramming/02_standard_dialog_boxes.html"""

speed = 5    
def main():
    global speed
    tess.forward(speed)
    if tess.xcor() >= 300:
        speed = -5
    if tess.xcor() <= -300:
        speed = 5
    wn.ontimer(main)

# These lines "wire up" keypresses to the handlers we’ve defined.
wn.onkey(fwd, "Up")
wn.onkey(rccw, "Left")
wn.onkey(rcw, "Right")
wn.onkey(qt, "Escape")
#Modifications:
wn.onkey(bwd, "Down")
wn.onkey(clr_red, "r")
wn.onkey(clr_green, "g")
wn.onkey(clr_blue, "b")
wn.onkey(line_plus, "+")
wn.onkey(line_minus, "-")
wn.onkey(pen_vis, "p")
wn.onkey(hlp, "F1")
wn.onkey(clear, "c")
wn.onkeypress(clrs, "Tab")
tess.onclick(onclick_shape)
tess.ondrag(drag)
tess.onrelease(release)
#################

# Now we need to tell the window to start listening for events,
# If any of the keys that we’re monitoring is pressed, its
# handler will be called.
wn.listen()
#main()
wn.mainloop()
