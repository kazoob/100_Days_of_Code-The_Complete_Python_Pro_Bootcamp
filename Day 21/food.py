from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "orange"


class Food(Turtle):
    x_min = None
    x_max = None
    y_min = None
    y_max = None

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")

        self.x_min = int(((screen_width / 2) - 20) * -1)
        self.x_max = int((screen_height / 2) - 40)
        self.y_min = int(((screen_width / 2) - 20) * -1)
        self.y_max = int((screen_height / 2) - 20)

        self.move()

    def move(self):
        x_pos = random.randint(self.x_min, self.x_max + 1)
        y_pos = random.randint(self.y_min, self.y_max + 1)

        self.teleport(x=x_pos, y=y_pos)
