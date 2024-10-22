from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    score = 0

    def __init__(self, screen_height):
        """Create a new scoreboard at the top of the screen, provided by screen_height."""
        super().__init__()
        # Set up scoreboard.
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.speed("fastest")

        # Position at top of the screen.
        y_pos = (screen_height / 2) - 25
        self.teleport(x=0, y=y_pos)

        # Draw the scoreboard.
        self.update_score()

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_score()

    def update_score(self):
        """Update the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        """Display the game over message."""
        self.teleport(x=0, y=0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
