from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def move_l(self):
        self.x_move = -abs(self.x_move)

    def move_r(self):
        self.x_move = abs(self.x_move)

    def wall_bounce(self):

        self.y_move *= -1

    def paddle_bounce(self):

        self.x_move *= -1
