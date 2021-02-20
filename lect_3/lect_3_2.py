import turtle

turtle.shape('turtle')
turtle.speed(4)
turtle.pensize(4)
turtle.color('blue')

digit_size = 30
digit_interval = 10
post_index = '223018'

# Converting the post index into a list of digits
post_index_list = list(map(int, list(post_index)))

# Base coordinates for each digit
coordinates_0 = [
    (0, digit_size * 2),
    (digit_size, digit_size * 2),
    (digit_size, 0),
    (0, 0),
    (0, digit_size * 2),
]
coordinates_1 = [
    (0, digit_size),
    (digit_size, digit_size * 2),
    (digit_size, 0),
]
coordinates_2 = [
    (0, digit_size * 2),
    (digit_size, digit_size * 2),
    (digit_size, digit_size),
    (0, 0),
    (digit_size, 0),
]
coordinates_3 = [
    (0, digit_size * 2),
    (digit_size, digit_size * 2),
    (0, digit_size),
    (digit_size, digit_size),
    (0, 0),
]
coordinates_4 = [
    (0, digit_size * 2),
    (0, digit_size),
    (digit_size, digit_size),
    (digit_size, digit_size * 2),
    (digit_size, 0),
]
coordinates_5 = [
    (digit_size, digit_size * 2),
    (0, digit_size * 2),
    (0, digit_size),
    (digit_size, digit_size),
    (digit_size, 0),
    (0, 0),
]
coordinates_6 = [
    (digit_size, digit_size * 2),
    (0, digit_size),
    (0, 0),
    (digit_size, 0),
    (digit_size, digit_size),
    (0, digit_size),
]
coordinates_7 = [
    (0, digit_size * 2),
    (digit_size, digit_size * 2),
    (0, digit_size),
    (0, 0),
]
coordinates_8 = [
    (0, digit_size),
    (0, digit_size * 2),
    (digit_size, digit_size * 2),
    (digit_size, 0),
    (0, 0),
    (0, digit_size),
    (digit_size, digit_size),
]
coordinates_9 = [
    (0, 0),
    (digit_size, digit_size),
    (digit_size, digit_size * 2),
    (0, digit_size * 2),
    (0, digit_size),
    (digit_size, digit_size),
]

# The list of coordinates, grouped for each digit
digit_range = [
    coordinates_0, coordinates_1, coordinates_2, coordinates_3, coordinates_4, coordinates_5,
    coordinates_6, coordinates_7, coordinates_8, coordinates_9,
]

def draw_digit(position, digit):
    """Print the required digit."""
    turtle.penup()
    for i in range(len(digit_range[digit])):
        x = digit_range[digit][i][0] + position * (digit_size + digit_interval)
        y = digit_range[digit][i][1]
        turtle.goto(x, y)
        turtle.pendown()


def print_post_index():
    """Call draw_digit function consistently."""
    for i in range(len(post_index_list)):
        draw_digit(i, post_index_list[i])


print_post_index()

turtle.done()
