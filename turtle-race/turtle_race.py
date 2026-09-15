from turtle import Turtle, Screen, TK
import random
import os

red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
purple = Turtle()

screen = Screen()
screen.screensize(500, 400)

turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_numbers = [0, 1, 2, 3, 4, 5]
turtle_coords = [(-225, 125), (-225, 75), (-225, 25), (-225, -25), (-225, -75), (-225, -125)]
i = 0

raceOver = False

os.system("clear")

bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour of the rainbow: ")

for turtle in screen.turtles():
    turtle.penup()
    turtle.color(turtle_colours[turtle_numbers[i]])
    turtle.shape("turtle")
    turtle.goto(turtle_coords[i])
    turtle.pendown()
    i += 1

while not raceOver:
    for turtle in screen.turtles():
        turtle.fd(random.randint(10,20))
        if turtle.xcor() >= 125:
            winner = turtle.color()[0]
            screen.bye()
            if bet == winner:
                TK.messagebox.showinfo(title="Outcome:", message="You guessed the correct turtle, good job!")
            else:
                TK.messagebox.showinfo(title="Outcome:", message="Im sorry you guessed the wrong turtle.")
                
os.system("clear")

