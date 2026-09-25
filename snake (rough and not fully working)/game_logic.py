from snake_movement import Movement
from snake_segment import Segment
from apple import Apple
from turtle import Screen
from time import sleep

class GameLogic:

    def __init__(self):

# Set up the screen

        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.title("Snake")
        self.screen.tracer(0)

# Set up the snake list

        self.segment = Segment()
        self.apple_create = Apple()
        self.segments = []
        self.apples = []

    def game_over(self):

# If any segment of the snake has an x or y coordinate at or beyond 300 it ends the game

        return any(abs(segment.xcor()) >= 300 or abs(segment.ycor()) >= 300 for segment in self.segments)

    def game_start(self):

# Set up the initial 3 snake segments

        for num in range(0, 3):
            self.snake_segment = self.segment.new_segment()
            self.segments.append(self.snake_segment)
            self.segments[num].bk(num*20)
            num += 1

# Update the screen after the segments are created

        self.screen.update()

        while True:
            for num in range(len(self.segments), 0, -1):
                num = num - 1
                self.movement = Movement(self.segments, self.screen)
                self.segments[num].fd(20)
                self.screen.onkey(self.movement.up, "w")
                self.screen.onkey(self.movement.down, "s")
                self.screen.onkey(self.movement.left, "a")
                self.screen.onkey(self.movement.right, "d")

# If apple doesnt exist create one

            if len(self.apples) == 0:
                self.apple = self.apple_create.new_apple()
                self.apples.append(self.apple)

# Remove apple if it comes in contact with snake

            if self.segments[0].pos() == self.apples[len(self.apples)-1].pos():
                self.apple.hideturtle()
                self.apples.pop(0)
                new_segment = self.segment.new_segment()
                new_segment.goto(self.segments[-1].pos())
                new_segment.setheading(self.segments[-1].heading() + 180)
                new_segment.forward(20)
                new_segment.setheading(self.segments[-1].heading())
                self.segments.append(new_segment)

# Game over conditions

            if self.game_over():
                self.screen.bye()
                break
            for i in range(len(self.segments)-1, 0, -1):
                if self.segments[0].pos() == self.segments[i].pos():
                    self.screen.bye()
                    break

            self.screen.update()
            sleep(0.1)
            
            


