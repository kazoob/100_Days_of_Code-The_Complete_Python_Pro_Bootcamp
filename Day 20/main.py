from turtle import Screen
from snake import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake Game"
SCREEN_BGCOLOR = "black"

SNAKE_INITIAL_LENGTH = 3
SNAKE_COLOR = "white"

scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH)
scr.title(SCREEN_TITLE)
scr.bgcolor(SCREEN_BGCOLOR)

snake = Snake(length=SNAKE_INITIAL_LENGTH, color=SNAKE_COLOR)

scr.listen()
scr.onkeypress(key="w", fun=snake.set_direction_up)
scr.onkeypress(key="s", fun=snake.set_direction_down)
scr.onkeypress(key="a", fun=snake.set_direction_left)
scr.onkeypress(key="d", fun=snake.set_direction_right)
scr.onkeypress(key="Up", fun=snake.set_direction_up)
scr.onkeypress(key="Down", fun=snake.set_direction_down)
scr.onkeypress(key="Left", fun=snake.set_direction_left)
scr.onkeypress(key="Right", fun=snake.set_direction_right)
scr.onkeypress(key="space", fun=snake.start)
scr.tracer(0)

while not snake.is_game_over():
    snake.move_forward()
    scr.update()
    time.sleep(0.1)

scr.exitonclick()
