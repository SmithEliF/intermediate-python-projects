from snake_movement import Movement
from snake_segment import Segment
from apple import Apple
from turtle import Screen, TK
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
        self.score = 0

    def on_apple(self):

# Return if the snake head is on an apple

        return self.segments[0].distance(self.apples[0]) < 15

    def game_over(self):

# Return if any segment of the snake has an x or y coordinate at or beyond 300

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


# If apple doesnt exist create one

        if len(self.apples) == 0:
            self.apple = self.apple_create.new_apple()
            self.apples.append(self.apple)

        while True:

# Move the snake forward

            self.movement = Movement(self.segments, self.screen)

# Move each segment of the snake to the one ahead of it

            for i in range(len(self.segments) - 1, 0, -1):
                self.segments[i].goto(self.segments[i - 1].pos())

                
# -1 selects the last segment in the list and gets the last tail position before the snake moves 
# so that the next added segment can replace it

            previous_tail_position = self.segments[-1].pos()

# Move the head of the snake forward

            self.segments[0].fd(20)

# Remove apple if it comes in contact with snake

            if self.on_apple():

# Add score

                self.score += 1

# Remove the previous apple

                self.apple.hideturtle()
                self.apples.pop(0)

# Create a new apple

                self.apple = self.apple_create.new_apple()
                self.apples.append(self.apple)

# Add a new segment

                new_segment = self.segment.new_segment()
                new_segment.goto(previous_tail_position)
                self.segments.append(new_segment)
                    
            self.screen.onkey(self.movement.up, "w")
            self.screen.onkey(self.movement.down, "s")
            self.screen.onkey(self.movement.left, "a")
            self.screen.onkey(self.movement.right, "d")

# Game over conditions

            if self.game_over():
                TK.messagebox.showinfo(title="Outcome:", message="You got a score of: " + str(self.score))
                self.screen.bye()
                break
            for i in range(len(self.segments)-1, 0, -1):
                if self.segments[0].distance(self.segments[i]) < 10:
                    TK.messagebox.showinfo(title="Outcome:", message="You got a score of: " + str(self.score))
                    self.screen.bye()
                    break

            self.screen.update()
            sleep(0.1)
            
            


