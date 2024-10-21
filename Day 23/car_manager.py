from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def move(self):
        for car in self.cars:
            if car.move_forward(self.move_distance) <= -340:
                self.cars.remove(car)
                car.remove()

        self.new_car()

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def new_car(self):
        self.cars.append(Car())


class Car:
    def __init__(self):
        color = random.choice(COLORS)
        y_pos = random.randint(-250, 260)

        self.front = self.new_section(color, 300, y_pos)
        self.back = self.new_section(color, 320, y_pos)

    def new_section(self, color, x_pos, y_pos):
        section = Turtle()
        section.shape("square")
        section.color(color)
        section.penup()
        section.setheading(180)
        section.speed("fastest")
        section.teleport(x=x_pos, y=y_pos)

        return section

    def move_forward(self, distance):
        self.front.forward(distance)
        self.back.forward(distance)

        return self.front.xcor()

    def remove(self):
        self.front.hideturtle()
        self.back.hideturtle()
