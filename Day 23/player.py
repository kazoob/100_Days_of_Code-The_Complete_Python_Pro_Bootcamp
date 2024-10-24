from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Create new player turtle at the bottom of the screen."""
        super().__init__()

        # Create turtle.
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.speed("fastest")

        # Position turtle.
        self.reset_pos()

    def move_up(self):
        """Move player up."""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Move player down."""
        self.back(MOVE_DISTANCE)

    def is_finish_line(self):
        """Return True if player cross the finish line, otherwise False."""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_pos(self):
        """Position player at the bottom of the screen."""
        self.goto(STARTING_POSITION)
