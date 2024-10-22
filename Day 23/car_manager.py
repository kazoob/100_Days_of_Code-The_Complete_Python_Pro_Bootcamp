from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """Create car manager. Will spawn cars at random intervals as well as move cars across the screen."""
        self.move_distance = STARTING_MOVE_DISTANCE

        # Car list.
        self.cars = []

        # Create new car.
        self.new_car()

    def move(self, new_car):
        """Move all active cars."""
        for car in self.cars:
            # If car is off the screen, clear and remove from list.
            if car.move_forward(self.move_distance) <= -340:
                self.cars.remove(car)
                car.remove()

        # Spawn new car if requested.
        if new_car:
            self.new_car()

    def level_up(self):
        """Level up. Increase car movement speed."""
        self.move_distance += MOVE_INCREMENT

    def new_car(self):
        """Spawn a new car at a random y-axis coordinate."""
        self.cars.append(Car())

    def collision(self, player):
        """Return True if player collides with any active car. Otherwise return False."""
        for car in self.cars:
            if car.collision(player):
                return True

        return False


class Car:
    def __init__(self):
        """Create a new car object with front and back section at a random y-axis coordinate."""

        # Choose random color.
        color = random.choice(COLORS)

        # Choose random y-axis position.
        y_pos = random.randint(-250, 260)

        # Create front and back sections.
        # TODO Replace front/back sections with one stretched car (use turtle.shapesize())
        self.front = self.new_section(color, 300, y_pos)
        self.back = self.new_section(color, 320, y_pos)

    def new_section(self, color, x_pos, y_pos):
        """Create a new car section at the specified x_pos and y_pos."""

        # Set up turtle object,
        section = Turtle()
        section.shape("square")
        section.color(color)
        section.penup()
        section.setheading(180)
        section.speed("fastest")

        # Position turtle.
        section.teleport(x=x_pos, y=y_pos)

        # Return the turtle.
        return section

    def move_forward(self, distance):
        """Move car sections forward. Return new x-axis coordinates."""
        self.front.forward(distance)
        self.back.forward(distance)

        return self.front.xcor()

    def remove(self):
        """Remove car sections from the screen."""
        self.front.hideturtle()
        self.back.hideturtle()

    def collision(self, player):
        """Return True if player collides with either front or back sections. Otherwise return False."""
        if self.front.distance(player) < 20 or self.back.distance(player) < 20:
            return True

        return False
