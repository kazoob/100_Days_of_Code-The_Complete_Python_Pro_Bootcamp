from turtle import Turtle, Screen
import time
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake Game"
SCREEN_BGCOLOR = "black"

SNAKE_INITIAL_LENGTH = 3
SNAKE_COLOR = "white"


class Snake:
    turtles = []
    direction = "right"
    moving = False

    def __init__(self):
        for i in range(0, SNAKE_INITIAL_LENGTH):
            x_pos = -20 * i
            y_pos = 0

            turtle = Turtle(shape='square')
            # TODO remove colors
            if i == 0:
                turtle.color(SNAKE_COLOR)
            elif i == 1:
                turtle.color("red")
            else:
                turtle.color("blue")
            turtle.penup()
            turtle.speed(speed="fastest")
            turtle.teleport(x=x_pos, y=y_pos)

            self.turtles.append(turtle)

    def start(self):
        self.moving = True

    def move_forward(self):
        if self.moving:
            previous_x = None
            previous_y = None

            for t in self.turtles:
                if self.turtles.index(t) == 0:
                    new_x = t.xcor()
                    new_y = t.ycor()

                    if self.direction == "up":
                        new_y += 20
                    elif self.direction == "down":
                        new_y -= 20
                    elif self.direction == "left":
                        new_x -= 20
                    else:
                        new_x += 20
                else:
                    new_x = previous_x
                    new_y = previous_y

                previous_x = t.xcor()
                previous_y = t.ycor()
                t.teleport(x=new_x, y=new_y)

    def set_direction_up(self):
        self.direction = "up"

    def set_direction_down(self):
        self.direction = "down"

    def set_direction_left(self):
        self.direction = "left"

    def set_direction_right(self):
        self.direction = "right"

    def is_game_over(self):
        return False


scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_WIDTH)
scr.title(SCREEN_TITLE)
scr.bgcolor(SCREEN_BGCOLOR)

snake = Snake()

scr.listen()
scr.onkeypress(key="w", fun=snake.set_direction_up)
scr.onkeypress(key="s", fun=snake.set_direction_down)
scr.onkeypress(key="a", fun=snake.set_direction_left)
scr.onkeypress(key="d", fun=snake.set_direction_right)
scr.onkeypress(key="space", fun=snake.start)
scr.tracer(0)

while not snake.is_game_over():
    snake.move_forward()
    scr.update()
    time.sleep(0.1)

scr.exitonclick()
