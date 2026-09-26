from screen import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

# Create screen elements

screen = Screen()
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

# Set that holds pressed keys

pressed_keys = set()

screen.screen.listen()

# Lambdas that track pressed keys

screen.screen.onkeypress(lambda: pressed_keys.add("w"), "w")
screen.screen.onkeyrelease(lambda: pressed_keys.discard("w"), "w")
screen.screen.onkeypress(lambda: pressed_keys.add("s"), "s")
screen.screen.onkeyrelease(lambda: pressed_keys.discard("s"), "s")
screen.screen.onkeypress(lambda: pressed_keys.add("Up"), "Up")
screen.screen.onkeyrelease(lambda: pressed_keys.discard("Up"), "Up")
screen.screen.onkeypress(lambda: pressed_keys.add("Down"), "Down")
screen.screen.onkeyrelease(lambda: pressed_keys.discard("Down"), "Down")

def update_game():
    global left_score, right_score

# Movement keys

    if "w" in pressed_keys:
        paddle_left.paddle_up()
    if "s" in pressed_keys:
        paddle_left.paddle_down()
    if "Up" in pressed_keys:
        paddle_right.paddle_up()
    if "Down" in pressed_keys:
        paddle_right.paddle_down()

# Move ball

    ball.move()

# Detect collision with wall

    if abs(ball.ycor()) > 280:
        ball.wall_bounce()

# Detect collision with paddle

    if ball.xcor() > 330 and ball.distance(paddle_right) < 50 or ball.xcor() < -330 and ball.distance(paddle_left) < 50:
        ball.paddle_bounce()
        ball.y_move += 0.5
        ball.x_move += 0.5

# Detect if right misses

    if ball.xcor() > 400:

# Resets ball, adds score, and flips serve direction 
    
        ball.goto(0, 0)
        scoreboard.l_point()
        ball.move_l()
        scoreboard.update_scoreboard()
        ball.x_move = 5
        ball.y_move = 5

# Detect if left misses

    if ball.xcor() < -400:

# Resets ball, adds score, and flips serve direction 

        ball.goto(0, 0)
        scoreboard.r_point()
        ball.move_r()
        scoreboard.update_scoreboard()
        ball.x_move = 5
        ball.y_move = 5

# Update game

    screen.screen.update()
    screen.screen.ontimer(update_game, 20)


update_game()
screen.screen.mainloop()