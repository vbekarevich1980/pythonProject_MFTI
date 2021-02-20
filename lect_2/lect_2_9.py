import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(3)
poly_num = 10
poly_r = 30
poly_v = 3
poly_r_incr = 20


def draw_polygon(n, r, r_i):
    turtle.left(90)
    turtle.circle(r, 360, n)
    turtle.right(90)
    turtle.penup()
    turtle.forward(r_i)
    turtle.pendown()


for i in range(0, poly_num):
    draw_polygon(poly_v, poly_r, poly_r_incr)
    poly_v += 1
    poly_r += poly_r_incr

turtle.done()
