from turtle import Turtle

TURTLE_SHAPE = "square"

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    turtles = []
    head = None
    moving = False
    color = None

    x_min = None
    x_max = None
    y_min = None
    y_max = None

    def __init__(self, length, color, screen_width, screen_height):
        self.color = color

        self.x_min = int(((screen_width / 2) - 20) * -1)
        self.x_max = int((screen_height / 2) - 20)
        self.y_min = int(((screen_width / 2) - 20) * -1)
        self.y_max = int((screen_height / 2) - 20)

        for i in range(0, length):
            x_pos = -20 * i
            y_pos = 0

            self.add_piece(x_pos, y_pos)

    def start_stop(self):
        self.moving = not self.moving

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

    def add_piece(self, x_pos, y_pos):
        turtle = Turtle(shape=TURTLE_SHAPE)
        turtle.color(self.color)
        turtle.penup()
        turtle.speed(speed="fastest")
        turtle.teleport(x=x_pos, y=y_pos)

        if not self.turtles:
            self.head = turtle

        self.turtles.append(turtle)

    def food_collected(self):
        x_pos = self.turtles[-1].xcor()
        y_pos = self.turtles[-1].ycor()

        self.add_piece(x_pos, y_pos)

    def is_game_over(self):
        if self.head.xcor() > self.x_max:
            return True
        elif self.head.xcor() < self.x_min:
            return True
        elif self.head.ycor() < self.y_min:
            return True
        elif self.head.ycor() < self.y_min:
            return True
        else:
            return False
