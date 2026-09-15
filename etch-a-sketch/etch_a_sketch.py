from turtle import Turtle, Screen

tim = Turtle()
tim.pencolor("black")
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()

screen.listen()

screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clear_screen, "space")

screen.exitonclick()
