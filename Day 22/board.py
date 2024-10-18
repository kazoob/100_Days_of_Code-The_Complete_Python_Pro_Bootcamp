from turtle import Turtle

LINE_SPACING = 20
LINE_THICKNESS = 3
LINE_COLOR = "white"


class Board(Turtle):

    def __init__(self, screen_height):
        """Create a new board with a center line down the middle, provided by screen_height."""
        super().__init__()

        # Set up the turtle.
        self.color(LINE_COLOR)
        self.speed("fastest")
        self.hideturtle()
        self.pensize(LINE_THICKNESS)

        # Turn off screen updates until completed.
        self.screen.tracer(0)

        # Draw the center line.
        y_max = int(screen_height / 2)
        y_min = -y_max

        # Start at the bottom of the screen.
        self.teleport(x=0, y=y_min)
        self.pendown()

        # Move to top of the screen.
        for y_pos in range(y_min, y_max + 1, LINE_SPACING):
            self.goto(x=0, y=y_pos)

            # Draw the dashes.
            if self.isdown():
                self.penup()
            else:
                self.pendown()

        # Update the screen.
        self.screen.tracer(1)
