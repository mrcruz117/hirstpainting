from turtle import Turtle, Screen
import random

TURTLE_SIZE = 20
yertle = Turtle(shape="turtle")

yertle.speed(0)
screen = Screen()
screen.colormode(255)
yertle.penup()
starting_pos = (-200, -200)
yertle.goto(starting_pos[0], starting_pos[1])
rgb_colors = [(132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71)]

dot_spacing = 40
dot_size = 15


def line_of_dots(num):
    for number in range(num):
        color = random.choice(rgb_colors)
        yertle.dot(dot_size, color)
        yertle.forward(dot_spacing)


def painting(dimension):
    for num in range(dimension):
        line_of_dots(dimension)
        yertle.back(dot_spacing * dimension)
        yertle.left(90)
        yertle.forward(dot_spacing)
        yertle.right(90)


painting(10)
screen.exitonclick()
