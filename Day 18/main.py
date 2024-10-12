from turtle import Turtle, Screen
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)

def rand_color(list):
    return random.choice(list)

rgb_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

ROWS = 10
COLS = 10
DOT_SIZE = 20
SPACING = 50

scr = Screen()
scr.colormode(255)

turt = Turtle()
turt.shape("turtle")
turt.speed("fastest")
turt.penup()

for r in range(0, ROWS):
    for c in range(0, COLS):
        x = (scr.canvwidth * -1) + (c * SPACING)
        y = (scr.canvheight * -1) + (r * SPACING)
        turt.teleport(x, y)

        turt.dot(DOT_SIZE, rand_color(rgb_colors))





scr.exitonclick()