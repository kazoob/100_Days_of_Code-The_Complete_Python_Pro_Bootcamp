from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self, screen_height):
        """Create a new scoreboard at the top of the screen, provided by screen_height."""
        super().__init__()

        # Set up variables.
        self.score = 0
        self.highscore = 0

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
        self.write(f"Score: {self.score} - High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        """Save the new high score if applicable and reset the score."""
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_score()
