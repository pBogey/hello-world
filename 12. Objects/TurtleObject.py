import turtle # Allows us to use turtles
window = turtle.Screen() # Creates a playground for turtles
window.bgcolor("gold") # Set the window background color
window.title("Turtle Objects") # Set the window title
turtle.screensize(200,200)
alex = turtle.Turtle() # Create a turtle, assign to alex
alex.color("red")
alex.penup()
alex.setposition(-150,0)
alex.pendown()
alex.pensize(3)
alex.begin_fill()
alex.write("Alex's id is:")
alex.forward(65)
alex.write(id(alex))
alex.forward(100)

tess = alex
tess.color("green")
tess.forward(100)
tess.write("Tess's id is:")
tess.forward(65)
tess.write(id(tess))
turtle.exitonclick()

