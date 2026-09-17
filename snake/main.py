from turtle import Screen
from game_logic import GameLogic


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
screen.title("Snake")

game_logic = GameLogic()

game_logic.game_start()
