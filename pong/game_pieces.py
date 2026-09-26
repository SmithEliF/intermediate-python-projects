from turtle import Turtle

class Paddle:

    def __init__(self):
        pass

    def create_paddle(self):

# Initialize paddle

        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(5, 1)