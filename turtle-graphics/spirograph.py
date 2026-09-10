import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed(200)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour = (r,g,b)

    return colour

directions = [0, 90, 180, 270]

while True:
    timmy.color(random_colour())
    timmy.right(10)
    timmy.circle(100)

