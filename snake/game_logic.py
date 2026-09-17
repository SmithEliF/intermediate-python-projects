from snake_movement import Movement
from snake_segment import Segment
from turtle import Screen

class GameLogic:

    def __init__(self):

        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.title("Snake")

        self.segment = Segment()
        self.segments = []

    def game_start(self):
        self.movement = Movement(self.segment)

        for num in range(0, 3):
            self.snake_segment = self.segment.new_segment()
            self.segments.append(self.snake_segment)
            self.segments[num].bk(num*20)
            num += 1

        while True:
            for num in range(0, len(self.segments)):
                self.segments[num].fd(20)


