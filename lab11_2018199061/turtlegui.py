import turtle
cellwidth = 30
cellheight = 30
size = 5
screensize = (cellheight*size, cellwidth*size)
turtle.setup(screensize[0], screensize[1])
turtle.screensize(screensize[0], screensize[1])
turtle.setworldcoordinates(0, 0, screensize[0], screensize[1])

t = turtle.Turtle()
t.speed(0)  # fastest turtle speed
t.hideturtle()
t.penup()
data = [[0,1,0,1,0],[1,0,0,0,1],[0,1,0,1,0],[1,0,0,0,1],[1,1,0,1,1]]
for i in range(len(data)):
    row = data[i]
    for j in range(len(row)):
        t.setposition(cellwidth*j, screensize[1]-cellheight*i)  # top-left
        t.pendown()
        if data[i][j] == 1:
            t.begin_fill()
        t.setheading(0)
        t.forward(cellwidth)
        t.setheading(-90)
        t.forward(cellheight)
        t.setheading(-180)
        t.forward(cellwidth)
        t.setheading(90)
        t.forward(cellheight)
        if data[i][j] == 1:
            t.end_fill()
        t.penup()
turtle.done()
