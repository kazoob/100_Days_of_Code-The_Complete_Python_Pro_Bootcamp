from turtle import Screen
from board import Board
from scoreboard import Scoreboard

# Set screen options.
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"
SCREEN_BGCOLOR = "black"

# Initialize screen.
scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.title(SCREEN_TITLE)
scr.bgcolor(SCREEN_BGCOLOR)

# Initialize board.
board = Board(screen_height=SCREEN_HEIGHT)

# Initialize scoreboard.
scoreboard = Scoreboard(screen_height=SCREEN_HEIGHT)

# Set up screen keyboard listening.
scr.listen()

# Run game until game over.
game_over = False
# while not game_over:

# Leave screen visible until mouse click.
scr.exitonclick()
