from turtle import Turtle

ALIGN = "center"
FONT_SIZE = 60
FONT = ('Courier', FONT_SIZE, 'normal')


class Scoreboard(Turtle):
    player1_score = 0
    player2_score = 0

    def __init__(self, screen_height):
        """Create a new scoreboard at the top of the screen, provided by screen_height."""
        super().__init__()

        # Set up scoreboard.
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")

        # Position at top of the screen.
        y_pos = (screen_height / 2) - (FONT_SIZE + 10)
        self.teleport(x=0, y=y_pos)

        # Draw the initial score.
        self.update_score()

    def update_score(self):
        """Update the scoreboard."""
        self.clear()
        self.write(f"{self.player1_score}  {self.player2_score}", align=ALIGN, font=FONT)

    def player1_point(self):
        """Give player 1 a point."""
        self.player1_score += 1
        self.update_score()

    def player2_point(self):
        """Give player 2 a point."""
        self.player2_score += 1
        self.update_score()
