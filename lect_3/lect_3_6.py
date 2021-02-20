from random import randint
import turtle


number_of_molecules = 10
steps_of_time_number = 1000

container_width = 300
container_height = 200


def draw_container(width, height):
    """Draw a container for gas"""
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.pensize(4)
    turtle.goto(-width / 2, -height / 2)
    turtle.pendown()
    turtle.goto(-width / 2, height / 2)
    turtle.goto(width / 2, height / 2)
    turtle.goto(width / 2, -height / 2)
    turtle.goto(-width / 2, -height / 2)


def fill_gas(num_molecules, speed=0, width=200, height=200):
    """Fill the container with gas"""
    container = [turtle.Turtle(shape='circle', visible=False) for i in range(num_molecules)]
    for unit in container:
        unit.penup()
        unit.speed(speed)
        unit.goto(randint(-int(width / 2), int(width / 2)), randint(-int(height / 2), int(height / 2)))
        unit.shapesize(0.5, 0.5)
        unit.setheading(randint(0, 360))
        unit.showturtle()
    return container


def walls_collision(width, height, molecules):
    """Check the possible collision with the walls of the container and change the angle in case of"""
    for unit in molecules:
        x, y = unit.position()
        angle = unit.heading()
        if x < -width / 2 or x > width / 2:
            unit.setheading(180 - angle)
        elif y < -height / 2 or y > height / 2:
            unit.setheading(-angle)


def gas_moving(molecules, distance=2):
    """Move the molecules on set distance"""
    for unit in molecules:
        unit.forward(distance)


draw_container(container_width, container_height)
filled_container1 = fill_gas(number_of_molecules, 10, container_width, container_height)
filled_container2 = fill_gas(number_of_molecules, 1, container_width, container_height)
for i in range(steps_of_time_number):
    walls_collision(container_width, container_height, filled_container1)
    gas_moving(filled_container1, 3)
    walls_collision(container_width, container_height, filled_container2)
    gas_moving(filled_container2)
