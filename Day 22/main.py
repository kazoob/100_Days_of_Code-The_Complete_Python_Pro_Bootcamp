from turtle import Screen
from board import Board
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set screen options.
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BGCOLOR = "black"


def start_round():
    time.sleep(0.5)

    player_win = 0
    while player_win == 0:
        ball.move_ball()
        player_win = ball.score()

    if player_win == 1:
        scoreboard.player1_point()
    else:
        scoreboard.player2_point()

    ball.reset_ball()


# Initialize screen.
scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.title(SCREEN_TITLE)
scr.bgcolor(SCREEN_BGCOLOR)

# Initialize board.
board = Board(screen_height=SCREEN_HEIGHT)

# Initialize the paddles.
paddle1 = Paddle(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, player=1)
paddle2 = Paddle(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, player=2)

# Initialize the ball.
ball = Ball(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, player1=paddle1, player2=paddle2)

# Initialize scoreboard.
scoreboard = Scoreboard(screen_height=SCREEN_HEIGHT)

# Set up screen keyboard listening.
scr.listen()
scr.onkeypress(key="w", fun=paddle1.move_up)
scr.onkeypress(key="s", fun=paddle1.move_down)
scr.onkeypress(key="Up", fun=paddle2.move_up)
scr.onkeypress(key="Down", fun=paddle2.move_down)
scr.onkeypress(key="space", fun=start_round)

# Run game until game over.
game_over = False
# while not game_over:

# Leave screen visible until mouse click.
scr.exitonclick()
