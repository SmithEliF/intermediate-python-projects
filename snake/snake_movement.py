class Movement:

    def __init__(self, snake_segment):
        self.snake_segment = snake_segment

    def up(self):
        self.snake_segment.setheading(90)

    def down(self):
        self.snake_segment.setheading(270)

    def left(self):
        self.snake_segment.setheading(180)

    def right(self):
        self.snake_segment.setheading(0)