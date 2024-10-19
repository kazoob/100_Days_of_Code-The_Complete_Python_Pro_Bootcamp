from turtle import Turtle
import random
import time

BALL_SIZE = 0.75
BALL_SPEED = 3  # slow
BALL_COLOR = "white"


class Ball(Turtle):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    player1 = None
    player2 = None

    def __init__(self, screen_width, screen_height, player1, player2):
        """Create a new ball in the middle of the screen.
        screen_width and screen_height are used to calculate the x-axis and y-axis bounds."""
        super().__init__()

        # Save the paddles for collision detection.
        self.player1 = player1
        self.player2 = player2

        # Calculate axis bounds.
        self.x_max = int(screen_width / 2)
        self.x_min = -self.x_max
        self.y_max = int(screen_height / 2)
        self.y_min = -self.y_max

        # Set up the ball.
        self.shape("square")
        self.color(BALL_COLOR)
        self.speed(BALL_SPEED)
        self.penup()
        self.shapesize(stretch_wid=BALL_SIZE, stretch_len=BALL_SIZE)

        # Position the ball.
        self.teleport(x=0, y=0)

    def reset_ball(self):
        # Position the ball.
        self.teleport(x=0, y=0)

        # Wait 1 second
        time.sleep(1)

        # Start the ball.
        self.start_ball()

    def start_ball(self):
        # Choose a random starting direction.
        player_start = random.choice([0, 180])

        # Choose a random starting heading.
        heading = random.randint(-75, 75) + player_start

        # Set the heading.
        self.set_ball_heading(heading)

        # Start moving the ball.
        self.move_ball()

    def move_ball(self):
        # Check for screen collision.
        # Top of screen.
        if self.ycor() >= self.y_max:
            self.set_ball_heading(0 - self.heading())

        # Bottom of screen.
        if self.ycor() <= self.y_min + 20 * BALL_SIZE:
            self.set_ball_heading(360 - self.heading())

        # Check for paddle collision.
        if self.player1.ball_collision(self) or self.player2.ball_collision(self):
            if 0 < self.heading() < 180:
                self.set_ball_heading(180 - self.heading())
            else:
                self.set_ball_heading(540 - self.heading())

        # Move the ball one unit forward.
        self.forward(20 * BALL_SIZE)

        # Continue moving the ball.
        self.move_ball()

    def set_ball_heading(self, heading):
        """Set the ball heading. Disable screen updates during the change. Set tilt angle to prevent rotation."""
        # Disable screen updates.
        self.screen.tracer(0)

        self.speed("fastest")

        # Set the heading.
        self.setheading(heading)

        # Set the tilt angle to prevent rotation.
        self.tiltangle(-heading % 90)

        self.speed(BALL_SPEED)

        # Enable screen updates.
        self.screen.tracer(1)
