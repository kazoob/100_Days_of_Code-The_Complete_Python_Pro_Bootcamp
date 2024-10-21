import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    if player.is_finish_line():
        player.reset_pos()
        # TODO car level up

    # TODO cars

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
