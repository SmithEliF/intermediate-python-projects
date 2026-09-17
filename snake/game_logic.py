from snake_movement import Movement
from snake_segment import Segment

class GameLogic:

    def __init__(self):
        
        self.segment = Segment()
        self.segments = []

    def game_start(self):
        for num in range(0, 3):
            self.snake_segment = self.segment.new_segment()
            self.segments.append(self.snake_segment)
            self.segments[num].bk(num*20)
            num += 1

        while True:
            for num in range(0, len(self.segments)):
                self.segments[num].fd(20)

    # movement = Movement(snake_segment)

    # screen.onkey(movement.up, "w")
    # screen.onkey(movement.down, "s")
    # screen.onkey(movement.left, "a")
    # screen.onkey(movement.right, "d")