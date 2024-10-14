from turtle import Turtle

TURTLE_SHAPE = "square"

# Constants for headings.
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
        """Create a new snake, with a starting length and color. Provide screen_width and screen_height
        to be used for wall collision detection."""
        self.color = color

        # Set bounding for wall collision detection.
        self.x_min = int(((screen_width / 2) - 20) * -1)
        self.x_max = int((screen_height / 2) - 20)
        self.y_min = int(((screen_width / 2) - 20) * -1)
        self.y_max = int((screen_height / 2) - 20)

        # Create the starting snake pieces.
        for i in range(0, length):
            x_pos = -20 * i
            y_pos = 0
            self.add_piece(x_pos, y_pos)

    def start_stop(self):
        """Start or stop the snake movement."""
        self.moving = not self.moving

    def move_forward(self):
        """Move the snake forward one iteration."""
        if self.moving:
            # Start moving snake from back to front, excluding the head.
            for i in range(len(self.turtles) - 1, 0, -1):
                new_x = self.turtles[i - 1].xcor()
                new_y = self.turtles[i - 1].ycor()
                self.turtles[i].teleport(x=new_x, y=new_y)

            # Move the head forward one iteration in the previously set heading.
            self.head.forward(20)

    def set_direction_up(self):
        """Set heading to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def set_direction_down(self):
        """Set heading to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def set_direction_left(self):
        """Set heading to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def set_direction_right(self):
        """Set heading to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_piece(self, x_pos, y_pos):
        """Add a new piece to the snake at the position x_pos, y_pos."""
        # Create the new turtle piece.
        turtle = Turtle(shape=TURTLE_SHAPE)
        turtle.color(self.color)
        turtle.penup()
        turtle.speed(speed="fastest")
        turtle.teleport(x=x_pos, y=y_pos)

        # If this is the first piece, this is the head.
        if not self.turtles:
            self.head = turtle

        # Add the piece to the snake.
        self.turtles.append(turtle)

    def food_collected(self):
        """Expand the snake due to food collection."""
        # Add a new piece at the end of the snake.
        x_pos = self.turtles[-1].xcor()
        y_pos = self.turtles[-1].ycor()
        self.add_piece(x_pos, y_pos)

    def is_game_over(self):
        """Check for all game over conditions, return True if game over, otherwise False.
        Game over conditions are wall collisions or snake body collisions."""
        # Check for up collision.
        if self.head.xcor() > self.x_max:
            return True
        # Check for down collision.
        elif self.head.xcor() < self.x_min:
            return True
        # Check for left collision.
        elif self.head.ycor() < self.y_min:
            return True
        # Check for right collision.
        elif self.head.ycor() > self.y_max:
            return True
        else:
            # Check for head collision with the rest of the body.
            for t in self.turtles[1:]:
                if self.head.distance(t) < 10:
                    return True
            return False
