from turtle import Turtle, Screen
import random
import colorgram

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.tracer(0)


def print_art(color_palate_image):

    # colors = colorgram.extract(color_palate_image, 12)
    # color_list = []
    # for color in colors:
    #     color_list.append(tuple(color.rgb))
    # print(color_list)
    color_list = [(202, 172, 91), (151, 92, 47), (219, 201, 101), (139, 19, 6), (194, 144, 42), (23, 10, 12), (181, 158, 174), (144, 151, 186), (218, 197, 210), (64, 95, 122)]

    def draw_grid(num_dots_row, num_dots_col):
        full_width = screen.window_width()
        full_height = screen.window_height()
        space_row = int(full_width / num_dots_row) * (1 - 1/num_dots_row)
        space_col = int(full_height / num_dots_col) * (1 - 1/num_dots_col)
        t.hideturtle()
        t.up()
        t.setposition((-full_width / 2 + space_row, full_height / 2 - space_col))
        for x in range(num_dots_col):
            for _ in range(num_dots_row):
                t.dot(20, random.choice(color_list))
                t.forward(space_row)
            t.setposition((-full_width / 2 + space_row), t.pos()[1]-space_col)

    draw_grid(10, 10)


print_art("docs/image.jpg")
screen.exitonclick()