import turtle
from random import *


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
turtle.color('red')


def random_moving1():
    """Makes the turtle move chaotic with turns and distances"""
    steps = randint(30, 70)

    for i in range(1, steps):
        turn = randint(1, 2)
        angle = randint(0, 360)

        if turn == 1:
            turtle.left(angle)
        else:
            turtle.right(angle)

        step = randint(0, 100)
        turtle.forward(step)


def random_moving2():
    """Makes the turtle move chaotic within determined coordinates"""
    steps = randint(30, 70)

    for i in range(1, steps):
        x = randint(-300, 300)
        y = randint(-300, 300)
        turtle.goto(x, y)


random_moving1()

turtle.clear()

random_moving2()

turtle.done()
