# M2. Bouncing Balls with Changing Color
# Modify the bouncing balls simulation program so that each time a ball hits an edge of the turtle graphics screen, it changes color.
# M3. Bouncing Balls with Trailing Lines
# Modify the bouncing balls simulation program so that a trail is left on the screen of each ball’s path.

# Bouncing Balls Simulation Program

import turtle
import random
import time


def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False


def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width / 2:
        return True
    else:
        return False


def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False


def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False


def bounceBall(ball, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading = 360 - ball.heading()

    return new_heading


def createBalls(num_balls):
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)
        new_ball.pendown()
        new_ball.pencolor('black')
        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls

#
def changeColor(ball):
    """
    Changes the fillcolor of the given ball object into a different color
    :param ball (object): instance of Turtle in module turtle
    :return: None
    """
    colors = ['white', 'red', 'blue', 'green', 'yellow', 'gray', 'black']  # set of color
    ball_color = ball.fillcolor()  # get current fillcolor
    random_color = random.choice(colors)  # pick new color from colors(list)
    while ball_color == random_color:  # keep picking if the newly picked color equals the previous color
        random_color = random.choice(colors)
        print('identical color!')
    ball.fillcolor(random_color)  # set fillcolor of the object

# ---- main
# program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

# create balls
balls = createBalls(num_balls)

# set start time
start_time = time.time()

# begin simulation
terminate = False


while not terminate:
    for k in range(0, len(balls)):
        balls[k].forward(15)

        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right'))
            changeColor(balls[k])  # change color of the ball at collision
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left'))
            changeColor(balls[k])  # change color of the ball at collision
        elif atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'down'))
            changeColor(balls[k])  # change color of the ball at collision
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'up'))
            changeColor(balls[k])  # change color of the ball at collision

        if time.time() - start_time > num_seconds:
            terminate = True

# exit on close window
turtle.exitonclick()
