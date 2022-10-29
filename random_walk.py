from turtle import Turtle, Screen
from random import choice, randrange
draw = Turtle()
screen = Screen()
screen.colormode(255)

headings = [0, 90, 180, 270]
draw.pensize(10)
draw.speed(9)


def random_colour():
    color_code = (randrange(255),randrange(255),randrange(255))
    return color_code


for i in range(100):
    draw.color(random_colour())
    draw.setheading(choice(headings))
    draw.forward(20)

screen.exitonclick()
