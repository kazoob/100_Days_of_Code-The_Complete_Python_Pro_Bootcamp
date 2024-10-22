import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_SLEEP_DELAY = 0.1

CAR_SPAWN_FREQUENCY = 6

# Set up screen.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Frogger")
screen.tracer(0)

# Set up game components.
player = Player()
score = Scoreboard()
cars = CarManager()

# Enable key press listening.
screen.listen()
screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)
screen.onkeypress(key="Down", fun=player.move_down)

# Game loop.
game_is_on = True
move_count = 0

while game_is_on:
    # If player crossed finish line, level up.
    if player.is_finish_line():
        player.reset_pos()
        score.level_up()
        cars.level_up()

    # Move cars and spawn a new car every CAR_SPAWN_FREQUENCY'th loop.
    if move_count >= CAR_SPAWN_FREQUENCY:
        cars.move(True)
        move_count = 0
    # Move cars and don't spawn a new car.
    else:
        cars.move(False)
        move_count += 1

    # End game if player car collision.
    if cars.collision(player):
        game_is_on = False

    # Game loop delay.
    time.sleep(SCREEN_SLEEP_DELAY)

    # Update screen elements.
    screen.update()

# Game loop end, game over.
player.game_over()
game_over = GameOver()

# Keep screen up until mouse click.
screen.exitonclick()
