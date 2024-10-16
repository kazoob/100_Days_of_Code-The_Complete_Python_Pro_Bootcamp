from turtle import Turtle

LINE_SPACING = 20


class Board(Turtle):

    def __init__(self, screen_height):
        """Create a new board with a center line down the middle, provided by screen_height."""
        super().__init__()

        # Set up the turtle
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        # Turn off screen updates until completed.
        self.screen.tracer(0)

        # Draw the center line.
        y_max = int(screen_height / 2)
        y_min = -1 * int(screen_height / 2)

        # Draw a 3 pixel thick line.
        for x_pos in range(-1, 2):
            self.teleport(x=x_pos, y=y_min)
            self.pendown()

            # Draw line from y_min to y_max, alternating pendown and penup every LINE_SPACING
            for y_pos in range(y_min, y_max + 1, LINE_SPACING):
                self.goto(x=x_pos, y=y_pos)
                if self.isdown():
                    self.penup()
                else:
                    self.pendown()

        # Update the screen.
        self.screen.tracer(1)
