import turtle

turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(3)
spiral_step = 10
spiral_wall = 0

for i in range(1, 55):
    spiral_wall += spiral_step
    turtle.forward(spiral_wall)
    turtle.left(90)

turtle.done()
