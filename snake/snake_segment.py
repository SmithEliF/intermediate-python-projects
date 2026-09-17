from turtle import Turtle

class Segment:

    def __init__(self):
        pass

    def new_segment(self):
        self.snake_segment = Turtle()
        self.snake_segment.color("white")
        self.snake_segment.shape("square")
        self.snake_segment.pu()
        return self.snake_segment