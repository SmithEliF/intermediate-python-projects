from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

line_colors = ["red", "green", "blue", "purple", "pink", "black", "orange", "yellow"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3, 11):
    timmy.color(line_colors[shape_side-3])
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()

