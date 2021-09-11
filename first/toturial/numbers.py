# num = 100
#
# if num % 2 == 0:
#     print(f'the number {num} is even!')
# else:
#     print(f'the {num} is odd!')

import turtle
import random

# def draw_with_cyclic_iteration():
colors = ['green', 'cyan', 'orange', 'purple', 'red', 'yellow', 'white']

turtle.bgcolor('gray8')
turtle.pendown()
turtle.pencolor(random.choice(colors))

i = 0

while True:
    i = (i + 1) % 6
    turtle.pensize(i)
    turtle.forward(225)
    turtle.right(170)


    if i == 0:
        turtle.pencolor(random.choice(colors))
