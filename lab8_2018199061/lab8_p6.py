import turtle

def drawSquare(myturtle, x, y, a):
    """
    Draws a square which has a lower left corner of (x,y) and side length of a

    :param myturtle (object) : instance of Turtle
    :param x: x-coordinate of bottom-left point of square
    :param y: y-coordinate of bottom-left point of square
    :param a: length of square
    :return: None
    """
    myturtle.penup()
    myturtle.setposition(x, y)  # Move to bottom left corner
    myturtle.pendown()  # Start Drawing
    for move in range(4):  # draw each side of a square
        myturtle.forward(a)  # go ahead by a pixels
        myturtle.left(90)  # turn 90 degrees left
    myturtle.penup()
