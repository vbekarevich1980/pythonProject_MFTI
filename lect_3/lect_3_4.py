import turtle


turtle.hideturtle()
turtle.penup()
turtle.goto(500, 0)
turtle.pendown()
turtle.pensize(4)
turtle.goto(-300, 0)

turtle.shape('circle')
turtle.shapesize(0.7, 0.7)
turtle.showturtle()
turtle.pensize(2)
turtle.speed(3)

x = -300
y = 0.000000001
Vx = 5
Vy = 12
dt = 0.5
ay = -0.9
ax = -0.02


while Vx > 0 or y != 0:
    turtle.goto(x, y)
    y += Vy * dt + ay * dt ** 2 / 2
    if y <= 0:
        y = 0
        Vy = -Vy
    x += Vx * dt
    Vy += ay * dt
    Vx += ax * dt
turtle.done()
