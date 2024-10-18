from turtle import Turtle

SCREEN_OFFSET = 100

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 4
PADDLE_COLOR = "white"


class Paddle(Turtle):
    y_min = 0
    y_max = 0

    player = 0

    def __init__(self, screen_width, screen_height, player):
        """Create a new paddle on the correct side for the provided player.
        screen_width is used to position the paddles.
        screen_height is used to calculate the y-axis bounds."""
        super().__init__()

        self.player = player

        # Calculate y-axis bounds.
        self.y_max = int(screen_height / 2)
        self.y_min = -self.y_max

        # Set up the paddle.
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_HEIGHT, stretch_len=PADDLE_WIDTH)

        # Position paddle on correct side according to player.
        if self.player == 1:
            x_pos = int(-screen_width / 2) + SCREEN_OFFSET
        else:
            self.setheading(180)
            x_pos = int(screen_width / 2) - SCREEN_OFFSET

        self.teleport(x=x_pos, y=0)

    def move_up(self):
        """Moves the paddle up. Will not exceed screen bounds."""
        y_pos = self.ycor() + 40
        if y_pos < self.y_max:
            self.sety(y_pos)

    def move_down(self):
        """Moves the paddle up. Will not exceed screen bounds."""
        y_pos = self.ycor() - 40
        if y_pos > self.y_min:
            self.sety(y_pos)

    def ball_collision(self, ball):
        # TODO better detection
        # Calculate paddle y-axis range.
        paddle_x_right = self.xcor() + 20 * PADDLE_WIDTH / 2
        paddle_x_left = self.xcor() - 20 * PADDLE_WIDTH / 2

        # Check for x-axis collision.
        if paddle_x_left <= ball.xcor() <= paddle_x_right:

            # Calculate paddle y-axis range.
            paddle_y_top = self.ycor() + 20 * PADDLE_HEIGHT / 2
            paddle_y_bot = self.ycor() - 20 * PADDLE_HEIGHT / 2

            # Check for y-axis collision.
            if paddle_y_bot <= ball.ycor() <= paddle_y_top:
                return True

        return False
