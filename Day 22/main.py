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

# Set game options.
START_DELAY = 0.5


def start_round():
    """Start a new round. While a player has not scored, continue moving the ball."""
    # Reset ball to center of the screen.
    ball.reset_ball()

    # Short pause
    time.sleep(START_DELAY)

    # Loop while a player has not scored, move ball.
    player_win = 0
    while player_win == 0:
        ball.move_ball()

        # Check if player has scored.
        player_win = ball.score()

    # Player 1 has scored.
    if player_win == 1:
        # Increase player 1 score.
        scoreboard.player1_point()
    # Player 2 has scored.
    elif player_win == 2:
        # Increase player 2 score.
        scoreboard.player2_point()

    # Round over, reset ball to center of the screen.
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

# Leave screen visible until mouse click.
scr.exitonclick()
