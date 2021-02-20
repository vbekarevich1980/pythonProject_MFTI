import turtle


turtle.shape('turtle')
turtle.speed(8)
turtle.pensize(2)
face_r = 200
eye_r = 30
mouth_r = 100


def draw_circle(size, color):
    turtle.color('black', color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def draw_arc(size, color):
    turtle.pencolor(color)
    turtle.circle(size, 180)


# Drawing face
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
draw_circle(face_r, 'yellow')
turtle.penup()

# Setting base point
x = turtle.xcor()
y = turtle.ycor()

# Drawing eyes
turtle.goto(x - face_r / 3, y + face_r / 3 * 4)
turtle.pendown()
draw_circle(eye_r, 'blue')
turtle.penup()
turtle.goto(x + face_r / 3, y + face_r / 3 * 4)
turtle.pendown()
draw_circle(eye_r, 'blue')
turtle.penup()

# Drawing nose
turtle.goto(x, y + face_r / 3 * 3)
turtle.right(90)
turtle.pensize(15)
turtle.pendown()
turtle.forward(50)
turtle.penup()

# Drawing smile
turtle.goto(x - mouth_r / 1 * 1, y + face_r / 3 * 2)
turtle.pendown()
draw_arc(mouth_r, 'red')
turtle.penup()

turtle.done()
