from turtle import Turtle
import random
import time

BALL_SIZE = 0.75
BALL_SPEED = 3 # slow


class Ball(Turtle):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    def __init__(self, screen_width, screen_height):
        """Create a new ball in the middle of the screen.
        screen_width and screen_height are used to calculate the x-axis and y-axis bounds."""
        super().__init__()

        # Calculate axis bounds.
        self.x_max = int(screen_width / 2)
        self.x_min = -1 * int(screen_width / 2)
        self.y_max = int(screen_height / 2)
        self.y_min = -1 * int(screen_height / 2)

        # Set up the ball
        self.shape("square")
        self.color("white")
        self.speed(BALL_SPEED)
        self.penup()
        self.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)

        # Position the ball
        self.teleport(x=0, y=0)

    def start(self):
        # Choose a random starting direction.
        player_start = random.choice([0, 180])

        # Choose a random starting heading.
        heading = random.randint(-75, 75) + player_start

        # Set the heading.
        self.speed("fastest")
        self.setheading(heading)
        self.speed(BALL_SPEED)

        # Start moving the ball
        self.move()

    def move(self):
        # Move the ball one unit forward
        self.forward(20 * BALL_SIZE)

        # Continue moving the ball
        self.move()
