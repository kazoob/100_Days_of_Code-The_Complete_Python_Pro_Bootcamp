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
        """Create a new Food item and display it on the screen, within the bounds of screen_width and screen_height."""
        super().__init__()

        # Create new food.
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.speed("fastest")
        # Set food size.
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        # Set bounding for food items.
        self.x_min = int(((screen_width / 2) - 20) * -1)
        self.x_max = int((screen_height / 2) - 40)
        self.y_min = int(((screen_width / 2) - 20) * -1)
        self.y_max = int((screen_height / 2) - 20)

        # Place food on screen.
        self.move()

    def move(self):
        """Place food randomly on screen."""
        # Generate random x and y coordinate.
        x_pos = random.randint(self.x_min, self.x_max + 1)
        y_pos = random.randint(self.y_min, self.y_max + 1)

        # Move food.
        self.teleport(x=x_pos, y=y_pos)
