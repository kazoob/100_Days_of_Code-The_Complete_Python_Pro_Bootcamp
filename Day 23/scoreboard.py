from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Create new scoreboard."""
        super().__init__()

        # Set up turtle object.
        self.hideturtle()
        self.color("black")
        self.penup()
        self.speed("fastest")

        # Position in top left corner of the screen.
        self.teleport(x=-290, y=270)

        # Starting level.
        self.level = 1

        # Print the level.
        self.print_level()

    def print_level(self):
        """Print the current level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        """Level up and print the new level on the screen."""
        self.level += 1
        self.print_level()


class GameOver(Turtle):
    def __init__(self):
        """Display game over message on the screen."""
        super().__init__()

        self.hideturtle()
        self.color("black")
        self.penup()
        self.speed("fastest")

        self.teleport(x=0, y=-150)

        self.write("Game over", align="center", font=FONT)
