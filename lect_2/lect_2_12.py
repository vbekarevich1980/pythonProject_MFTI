import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
spring_r1 = 50
spring_r2 = 10
spring_num = 5


def draw_spring(size1, size2):
    turtle.circle(-size1, 180)
    turtle.circle(-size2, 180)


turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)

for i in range(0, spring_num-1):
    draw_spring(spring_r1, spring_r2)

turtle.circle(-spring_r1, 180)
turtle.done()
