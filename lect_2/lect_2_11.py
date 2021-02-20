import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
butterfly_r = 70
butterfly_wings = 20
butterfly_color = ('red', 'blue')


def draw_butterfly(size):
    turtle.circle(size)
    turtle.circle(-size)


turtle.right(90)
for i in range(0, int(butterfly_wings/4)):
    turtle.pencolor(butterfly_color[0])
    draw_butterfly(butterfly_r)
    butterfly_r += 10
    turtle.pencolor(butterfly_color[1])
    draw_butterfly(butterfly_r)
    butterfly_r += 10


turtle.done()
