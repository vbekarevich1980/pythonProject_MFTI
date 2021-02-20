import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.pensize(2)
square_size = 20
square_gap = 20

for i in range(1, 11):
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.penup()
    turtle.goto(turtle.xcor()-square_gap, turtle.ycor()-square_gap)
    turtle.pendown()
    square_size += square_gap * 2

turtle.done()
