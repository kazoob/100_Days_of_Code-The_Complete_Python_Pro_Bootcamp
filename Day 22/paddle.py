from turtle import Turtle

SCREEN_OFFSET = 100

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 4


class Paddle(Turtle):
    y_min = 0
    y_max = 0

    def __init__(self, screen_width, screen_height, player):
        """Create a new paddle on the correct side for the provided player.
        screen_width is used to position the paddles.
        screen_height is used to calculate the y-axis bounds."""
        super().__init__()

        # Calculate y-axis bounds.
        self.y_max = int(screen_height / 2)
        self.y_min = -1 * int(screen_height / 2)

        # Set up the paddle
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)

        # Position paddle on correct side according to player
        if player == 1:
            x_pos = int(-1 * screen_width / 2) + SCREEN_OFFSET
        else:
            self.setheading(180)
            x_pos = int(screen_width / 2) - SCREEN_OFFSET

        self.teleport(x=x_pos, y=0)

    def move_up(self):
        """Moves the paddle up. Will not exceed screen bounds."""
        y_pos = self.ycor() + 20
        if y_pos < self.y_max:
            self.sety(y_pos)

    def move_down(self):
        """Moves the paddle up. Will not exceed screen bounds."""
        y_pos = self.ycor() - 20
        if y_pos > self.y_min:
            self.sety(y_pos)
