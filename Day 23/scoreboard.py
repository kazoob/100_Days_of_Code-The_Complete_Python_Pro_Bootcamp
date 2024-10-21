from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("black")
        self.penup()
        self.speed("fastest")

        self.teleport(x=-290, y=270)

        self.level = 1

        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.print_level()
