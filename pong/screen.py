from turtle import Screen as s

class Screen:

    def __init__(self):
        pass

    def create_screen(self):

# Initialize screen

        self.screen = s()
        self.screen.bgcolor("black")
        self.screen.setup(800, 600)
        self.screen.title("pong")

        self.screen.exitonclick()

        return self.screen