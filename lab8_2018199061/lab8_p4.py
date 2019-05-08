import turtle

# set window size
turtle.setup(800,600)

# get reference to turtle window
window = turtle.Screen()

# set window title bar
window.title('Problem 4')

# create a turtle and hide it
the_turtle = turtle.getturtle()
the_turtle.hideturtle()

# use pen attributes to draw
the_turtle.penup()  # stop drawing
the_turtle.setposition(-800, 600)  # move to top-left corner
the_turtle.pendown()  # start drawing
the_turtle.setposition(800, -600)  # move to bottom-right corner
the_turtle.penup()  # stop drawing
the_turtle.setposition(-800, -600)  # move to bottom-left corner
the_turtle.pendown()  # start drawing
the_turtle.setposition(800, 600)  # move to top-right corner

# prevent window from immediate closing
window.exitonclick()
