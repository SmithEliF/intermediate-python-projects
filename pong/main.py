from screen import Screen
from game_pieces import Paddle

screen = Screen()
paddle = Paddle()

screen.create_screen()
paddle.create_paddle()

screen.exit_on_click()