from turtle import Turtle
import random

class Apple:

    def __init__(self):
        pass

# Build the snake segments

    def new_apple(self, occupied_positions=None):
        self.apple = Turtle()
        self.apple.color("red")
        self.apple.shape("square")
        self.apple.pu()
        self.apple.speed(10000)

        occupied_positions = occupied_positions or []

        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            x = x - (x % 20)
            y = y - (y % 20)

            if (x, y) not in occupied_positions:
                self.apple.goto(x, y)
                return self.apple