from turtle import Turtle, Screen
from random import randrange

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        draw.forward(100)
        draw.right(angle)


def random_colour():
    color_code = (randrange(255),randrange(255),randrange(255))
    return color_code


draw = Turtle()
screen = Screen()
screen.colormode(255)

for n in range(3, 11):
    draw.pencolor(random_colour())
    draw_shape(n)

screen.exitonclick()
