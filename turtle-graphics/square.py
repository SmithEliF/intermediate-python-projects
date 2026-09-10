from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

i = 0

while i < 4:
    timmy.forward(100)
    timmy.right(90)
    i += 1
    print("hi")

screen = Screen()
screen.exitonclick()