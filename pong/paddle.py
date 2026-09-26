from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):

# Initialize Paddle

        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.pu()
        self.goto(x, y)

    def paddle_up(self):

# Move the paddle up

        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def paddle_down(self):

# Move the paddle down

        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
