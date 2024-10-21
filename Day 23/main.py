import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)
screen.onkeypress(key="Down", fun=player.move_down)

game_is_on = True
while game_is_on:
    if player.is_finish_line():
        player.reset_pos()
        score.level_up()
        cars.level_up()

    cars.move()

    if cars.collision(player):
        game_is_on = False

    time.sleep(0.1)
    screen.update()

player.game_over()
game_over = GameOver()

screen.exitonclick()
