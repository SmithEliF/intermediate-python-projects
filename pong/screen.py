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

        return self.screen

    def exit_on_click(self):
            
        self.screen.exitonclick()