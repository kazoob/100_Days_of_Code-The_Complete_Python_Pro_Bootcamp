from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.speed("fastest")

        self.reset_pos()

        self.game_is_over = False

    def move_up(self):
        if not self.game_is_over:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if not self.game_is_over:
            self.back(MOVE_DISTANCE)

    def is_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.game_is_over = True
