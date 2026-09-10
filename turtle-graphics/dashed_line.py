from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

i = 0

while i < 50:
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    i += 1
    print("hi")

screen = Screen()
screen.exitonclick()