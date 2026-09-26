class Movement:

    def __init__(self, snake_segments, screen):
        self.snake_segments = snake_segments
        self.screen = screen
        
    def up(self):
        for i in range(len(self.snake_segments) - 1, -1, -1):
            self.delay = int(i / 10 * 1000)
            self.segment = self.snake_segments[i]
            self.screen.ontimer(lambda segment=self.segment: segment.setheading(90), self.delay)

    def down(self):
        for i in range(len(self.snake_segments) - 1, -1, -1):
            self.delay = int(i / 10 * 1000)
            self.segment = self.snake_segments[i]
            self.screen.ontimer(lambda segment=self.segment: segment.setheading(270), self.delay)

    def left(self):
        for i in range(len(self.snake_segments) - 1, -1, -1):
            self.delay = int(i / 10 * 1000)
            self.segment = self.snake_segments[i]
            self.screen.ontimer(lambda segment=self.segment: segment.setheading(180), self.delay)

    def right(self):
        for i in range(len(self.snake_segments) - 1, -1, -1):
            self.delay = int(i / 10 * 1000)
            self.segment = self.snake_segments[i]
            self.screen.ontimer(lambda segment=self.segment: segment.setheading(0), self.delay)