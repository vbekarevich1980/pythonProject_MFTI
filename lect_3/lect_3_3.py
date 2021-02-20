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

with open('digit_coordinates.txt', 'w') as file:
    for i in range(10):
        file.write(str(digit_range[i]) + '\r\n')

with open('digit_coordinates.txt', 'r') as file:
    digit_range_from_file = file.readlines()


def draw_digit(position, digit):
    """Print the required digit."""
    turtle.penup()
    digit_str = digit_range_from_file[digit].lstrip('[')
    digit_str = digit_str.rstrip()
    digit_str = digit_str.rstrip(']')
    digit_str = digit_str.replace('(', '')
    digit_str = digit_str.replace(')', '')
    digit_list = digit_str.split(', ')
    for step in range(int(len(digit_list) / 2)):
        x = int(digit_list[step * 2]) + position * (digit_size + digit_interval)
        y = int(digit_list[step * 2 + 1])
        turtle.goto(x, y)
        turtle.pendown()


def print_post_index():
    """Call draw_digit function consistently."""
    for d in range(len(post_index_list)):
        draw_digit(d, post_index_list[d])


print_post_index()
turtle.hideturtle()

turtle.done()
