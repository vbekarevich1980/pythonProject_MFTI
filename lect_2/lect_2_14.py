import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
star_r = 200
star_v = 25


def vertex_cor(size, vertices):
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    coordinates = [(turtle.xcor(), turtle.ycor())]
    for i in range(1, vertices):
        turtle.circle(-size, 360 / vertices)
        y = turtle.ycor()
        x = turtle.xcor()
        coordinates.append((x, y))
    return coordinates


def draw_star(size, vertices):
    ver_coors = vertex_cor(size, vertices)
    step1 = 0
    step2 = vertices // 2
    turtle.goto(ver_coors[step1])
    turtle.showturtle()
    turtle.pendown()
    turtle.speed(8)
    turtle.goto(ver_coors[step2])
    for i in range(0, vertices // 2):
        step1 -= 1
        step2 -= 1
        turtle.goto(ver_coors[step1])
        turtle.goto(ver_coors[step2])


turtle.penup()
turtle.goto(0, star_r)
draw_star(star_r, star_v)

turtle.done()
