import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
flower_r = 100
flower_petal = 8
flower_color = 'red'




def draw_flower(size, petals, color):
    turtle.pencolor(color)
    turtle.circle(size)
    turtle.circle(-size)
    turtle.left(360 / petals)


for i in range(0, int(flower_petal / 2)):
    draw_flower(flower_r, flower_petal, flower_color)


turtle.done()
