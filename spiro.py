from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed("fastest")


def random_colour():
    color_code = (random.randrange(255), random.randrange(255), random.randrange(255))
    return color_code

def draw_spirograph (size_of_gap):
    for x in range(int(360/size_of_gap)):
        t.circle(100, None, None)
        t.right(size_of_gap)
        t.color(random_colour())


draw_spirograph(5)

screen.exitonclick()
