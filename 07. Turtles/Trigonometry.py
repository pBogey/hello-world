"""
Turtle sine wave
13.10.2018 09:42
Bogdan Prădatu
"""

print("This program will plot a sine/cosine wave of the form Asin(wt+phi)+o")
print("Where A is the Amplitutde")
print("w is the Angular Frequency: w = 2*pi*f")
print("phi is the Phase of the wave")
print("o is the Offset of the midline\n")


# Define new function for keyboard input
def arguments(prompt_msg):
    while True:  # create loop for error check
        try:
            variable = float(input(prompt_msg))  # convert user input to float
        except ValueError:
            # if input is not a number, retry
            print("invalid number, please try again:")
            continue
        else:
            # user input was valid, end
            break
    return variable


def sine_wave():

    import turtle
    from math import sin
    from math import cos
    from math import pi
    from math import radians

    trig = int(arguments("Please input 1 for sine wave, 2 for cosine wave or 0 for both: "))
    A = arguments("Please input the desired amplitude of the wave: ")
    f = arguments("Please input the desired frequency of the wave: ")
    phi = arguments("Please input the desired phase of the wave: ")
    o = arguments("Please input the desired offset of the wave: ")

    window = turtle.Screen()                        # create turtle graphics screen
    window.bgcolor("honeydew")                      # set window background color
    window.title("Sine/Cosine")                     # set window title
    
    llx = -5                                        # define window coordinates
    if A >= 1:
        lly = -1.2*(A+abs(o))                       # as a function of wave amplitude
    else:
        lly = -1.2*(abs(o))  
    if f < 1:                                       # and wave offset
        urx = 1/f*70
    else:
        urx = 70
    if A >= 1:
        ury = 1.2*(A+abs(o))
    else:
        ury = 1.2*(abs(o))
    turtle.setworldcoordinates(llx, lly, urx, ury)  # set coordinates
    trt = turtle.Turtle()                           # create turtle
    trt.speed(0)                                    # set drawing speed
    trt.hideturtle()                                # hide turtle stamp
    trt.color("black")                              # define drawing color
    trt.penup()                                     # deactivate drawing
    if A >= 1:
        trt.setposition(0, -(A+abs(o)))             # move turtle to desired position
        trt.pendown()                               # allow drawing
        trt.left(90)
        y0 = -(A+abs(o))                            # create plot y axis
        for i in range(20):                         # use loop to draw axis and labels
            trt.penup()
            trt.left(90)
            trt.forward(3)
            trt.write(str(y0)[0:5])
            trt.right(180)
            trt.forward(3)
            trt.left(90)
            trt.pendown()
            trt.forward((A+abs(o))/10)
            y0 += (A+abs(o))/10
    else:
        trt.setposition(0, -(1+abs(o)))             # move turtle to desired position
        trt.pendown()                               # allow drawing
        trt.left(90)
        y0 = -(1+abs(o))
        for i in range(20):
            trt.penup()
            trt.left(90)
            trt.forward(3)
            trt.write(str(y0)[0:5])
            trt.right(180)
            trt.forward(3)
            trt.left(90)
            trt.pendown()
            trt.forward((1+abs(o))/10)
            y0 += (1+abs(o))/10
    trt.stamp()                                     # stamp axis end arrow
    if A >= 1:
        trt.penup()
        trt.left(90)
        trt.forward(3)
        trt.write(str(A+abs(o)))
    else:
        trt.penup()
        trt.left(90)
        trt.forward(3)
        trt.write(1)
    trt.setposition(0, 0)                           # move turtle to origin
    trt.right(180)                                  # and prepare for x axis draw
    x0 = 0                                          # and y axis
    if f < 1:                                       # define as a function of frequency
        ra = 12 * 1/f                               # longer axis for lower frequency
    else:                                           # so it can show a whole cycle
        ra = 12
    for i in range(int(ra)):
        trt.pendown()
        trt.forward(5)
        x0 += 5
        trt.penup()
        trt.right(90)
        trt.forward(A/10)
        trt.write(str(radians(x0))[0:5])
        trt.left(180)
        trt.forward(A/10)
        trt.right(90)
    trt.stamp()
    trt.penup()                                     # deactivate drawing
    trt.setposition(0, 0)                           # and move to origin
    trt.pensize(5)                                  # linewidth 5
    trt.color("orange")                             # line color = orange
    if f < 0:                                       # define sine wave length
        rw = 590 * 1/f                              # longer wave for low frequency
    else:                                           # to capture one period
        rw = 590                                    # 1pi radians for high frequency
    if trig == 1:                                   # define wave equation
        for t in range(0, int(rw)):
            y = A*sin(2*pi*f*radians(t/10)+phi)+o
            trt.goto(t/10, y)
            trt.pendown()
    elif trig == 2:
        for t in range(0, int(rw)):
            y = A*cos(2*pi*f*radians(t/10)+phi)+o
            trt.goto(t/10, y)
            trt.pendown()
    elif trig == 0:
        for t in range(0, int(rw)):
            trt.color("brown")
            y = A*sin(2*pi*f*radians(t/10)+phi)+o
            trt.goto(t/10, y)
            trt.pendown()
        trt.penup()
        trt.setposition(0, 0)
        for t in range(0, int(rw)):
            trt.color("SeaGreen")
            y = A*cos(2*pi*f*radians(t/10)+phi)+o
            trt.goto(t/10, y)
            trt.pendown()
        trt.penup()                                 # deactivate drawing
        if A >= 1:
            trt.setposition(0, -1.1*(A+abs(o)))          # prepare turtle for legend creation
        else:
            trt.setposition(0, -1.1)
        trt.color("brown")
        trt.write("sine", font=("Arial", 10, "bold"))
        if A >= 1:
            trt.setposition(0, -1.15*(A+abs(o)))
        else:
            trt.setposition(0, -1.15)
        trt.color("SeaGreen")
        trt.write("cosine", font=("Arial", 10, "bold"))
        trt.pendown()
    else:
        print("You didn't choose the right type of function")
        return

    answer = turtle.textinput("Done!", "Would you like to close the window now? (yes or no)")
    if answer == "yes":
        turtle.bye()
    elif answer == "no":
        turtle.mainloop()
    else:
        turtle.exitonclick()


sine_wave()


print("Goodbye!")
