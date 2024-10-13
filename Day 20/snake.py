from turtle import Turtle


class Snake:
    turtles = []
    head = None
    moving = False

    def __init__(self, length, color):
        for i in range(0, length):
            x_pos = -20 * i
            y_pos = 0

            turtle = Turtle(shape='square')
            turtle.color(color)
            turtle.penup()
            turtle.speed(speed="fastest")
            turtle.teleport(x=x_pos, y=y_pos)

            self.turtles.append(turtle)

            if i == 0:
                self.head = turtle

    def start(self):
        self.moving = True

    def move_forward(self):
        if self.moving:
            # Start moving snake from back to front
            for i in range(len(self.turtles) - 1, 0, -1):
                new_x = self.turtles[i - 1].xcor()
                new_y = self.turtles[i - 1].ycor()
                self.turtles[i].teleport(x=new_x, y=new_y)

            self.head.forward(20)

    def set_direction_up(self):
        self.head.setheading(90)

    def set_direction_down(self):
        self.head.setheading(270)

    def set_direction_left(self):
        self.head.setheading(180)

    def set_direction_right(self):
        self.head.setheading(0)

    def is_game_over(self):
        return False
