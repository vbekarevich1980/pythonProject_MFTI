import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.pensize(2)
spider_legs = 18
spider_size = 200

for i in range(1, spider_legs+1):
    turtle.forward(spider_size)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(360 / spider_legs)
    turtle.pendown()

turtle.done()
