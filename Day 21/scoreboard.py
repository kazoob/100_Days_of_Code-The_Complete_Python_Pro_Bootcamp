from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.speed("fastest")

        y_pos = (screen_height / 2) - 25

        self.teleport(x=0, y=y_pos)

        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))
