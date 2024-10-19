from turtle import Turtle
import random

BALL_SIZE = 0.75
BALL_SPEED = 3  # slow
BALL_COLOR = "white"

START_HEADING_CHOICE = 75

TURTLE_SIZE = 20


class Ball(Turtle):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    player1 = None
    player2 = None

    is_reset = False

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
        self.reset_ball()

    def reset_ball(self):
        """Reset the ball at the center of the screen. Choose a random starting direction and heading."""
        # Ball is reset.
        self.is_reset = True

        # Position the ball.
        self.teleport(x=0, y=0)

        # Choose a random starting direction.
        player_start = random.choice([0, 180])

        # Set a random starting heading.
        heading = random.randint(-START_HEADING_CHOICE, START_HEADING_CHOICE) + player_start
        self.set_ball_heading(heading)

    def move_ball(self):
        """Move the ball one unit forward. Check for top or bottom screen collision and change heading."""
        # Ball is no longer reset.
        if self.is_reset:
            self.is_reset = False

        # Move the ball one unit forward.
        self.forward(TURTLE_SIZE * BALL_SIZE)

        # Check for screen collision.
        # Top of screen.
        if self.ycor() >= self.y_max:
            self.set_ball_heading(0 - self.heading())

        # Bottom of screen.
        if self.ycor() <= self.y_min + TURTLE_SIZE * BALL_SIZE:
            self.set_ball_heading(360 - self.heading())

        # Check for paddle collision.
        if self.player1.ball_collision(self) or self.player2.ball_collision(self):
            if 0 < self.heading() < 180:
                self.set_ball_heading(180 - self.heading())
            else:
                self.set_ball_heading(540 - self.heading())

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

    def score(self):
        """Check if a player has scored. If yes, return player number.
        If none, return 0. If ball is reset, return -1."""
        # Check if ball is reset.
        if self.is_reset:
            return -1
        # Check if player 2 scored.
        elif self.xcor() <= self.x_min:
            return 2
        # Check if player 1 scored.
        elif self.xcor() >= self.x_max:
            return 1
        # No one has scored.
        else:
            return 0
