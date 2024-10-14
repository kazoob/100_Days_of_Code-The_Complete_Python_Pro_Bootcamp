from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set screen options.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake Game"
SCREEN_BGCOLOR = "black"

# Set snake options.
SNAKE_INITIAL_LENGTH = 3
SNAKE_COLOR = "white"

# Initialize screen.
scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.title(SCREEN_TITLE)
scr.bgcolor(SCREEN_BGCOLOR)

# Initialize snake.
snake = Snake(length=SNAKE_INITIAL_LENGTH, color=SNAKE_COLOR, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

# Initialize food.
food = Food(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

# Initialize scoreboard.
scoreboard = Scoreboard(screen_height=SCREEN_HEIGHT)

# Set up screen keyboard listening.
scr.listen()
scr.onkeypress(key="w", fun=snake.set_direction_up)
scr.onkeypress(key="s", fun=snake.set_direction_down)
scr.onkeypress(key="a", fun=snake.set_direction_left)
scr.onkeypress(key="d", fun=snake.set_direction_right)
scr.onkeypress(key="Up", fun=snake.set_direction_up)
scr.onkeypress(key="Down", fun=snake.set_direction_down)
scr.onkeypress(key="Left", fun=snake.set_direction_left)
scr.onkeypress(key="Right", fun=snake.set_direction_right)
scr.onkeypress(key="space", fun=snake.start_stop)

# Disable screen updates.
scr.tracer(0)

# Run game until game over.
game_over = False
while not game_over:
    # Move snake forward one iteration.
    snake.move_forward()

    # Check for food collision.
    if snake.head.distance(food) < 15:
        # Move food to different location.
        food.move()

        # Grow snake.
        snake.food_collected()

        # Increase score.
        scoreboard.increase_score()

    # Check for game over conditions. Either wall collision or snake body collision.
    if snake.is_game_over():
        # Break while loop.
        game_over = True

        # Display game over message.
        scoreboard.game_over()

    # Update screen.
    scr.update()

    # Game delay.
    time.sleep(0.1)

# Leave screen visible until mouse click.
scr.exitonclick()
