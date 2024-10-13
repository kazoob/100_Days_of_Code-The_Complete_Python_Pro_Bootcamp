from turtle import Turtle


class Snake:
    turtles = []
    direction = "right"
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

    def start(self):
        self.moving = True

    def move_forward(self):
        if self.moving:
            # Start moving snake from front to back
            # previous_x = None
            # previous_y = None
            #
            # for t in self.turtles:
            #     if self.turtles.index(t) == 0:
            #         new_x = t.xcor()
            #         new_y = t.ycor()
            #
            #         if self.direction == "up":
            #             new_y += 20
            #         elif self.direction == "down":
            #             new_y -= 20
            #         elif self.direction == "left":
            #             new_x -= 20
            #         else:
            #             new_x += 20
            #     else:
            #         new_x = previous_x
            #         new_y = previous_y
            #
            #     previous_x = t.xcor()
            #     previous_y = t.ycor()
            #     t.teleport(x=new_x, y=new_y)

            # Start moving snake from back to front
            for i in range(len(self.turtles) - 1, 0, -1):
                new_x = self.turtles[i - 1].xcor()
                new_y = self.turtles[i - 1].ycor()
                self.turtles[i].teleport(x=new_x, y=new_y)

            new_x = self.turtles[0].xcor()
            new_y = self.turtles[0].ycor()

            if self.direction == "up":
                new_y += 20
            elif self.direction == "down":
                new_y -= 20
            elif self.direction == "left":
                new_x -= 20
            else:
                new_x += 20

            self.turtles[0].teleport(x=new_x, y=new_y)

    def set_direction_up(self):
        self.direction = "up"

    def set_direction_down(self):
        self.direction = "down"

    def set_direction_left(self):
        self.direction = "left"

    def set_direction_right(self):
        self.direction = "right"

    def is_game_over(self):
        return False
