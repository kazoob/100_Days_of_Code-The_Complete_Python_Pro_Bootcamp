from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def set_direction_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def set_direction_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def set_direction_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_game_over(self):
        return False
