def drawFlower(myturtle, r):
    """ Draws a flower composed of 24 circles on the screen. The radius of the circles is ``r''.
    The drawing color is ``red''.
    The turtle ``myturtle'' is already
    positioned in the center of the flower.
    """
    # pendown and set color
    myturtle.pendown()
    myturtle.color('red')

    # start drawing, add 15 degrees to heading for each circle(360/24=15)
    for heading in range(0, 360, 15):
        myturtle.setheading(heading)
        myturtle.circle(r)
