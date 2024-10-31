from random import randint
from turtle import Turtle, Screen
import random

scr = Screen()
# rootwindow = scr.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
# rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

turt = Turtle()
turt.shape("turtle")
turt.color("orange")

# Challenge 1
# turt.forward(100)
# turt.right(90)
# turt.forward(100)
# turt.right(90)
# turt.forward(100)
# turt.right(90)
# turt.forward(100)

# for i in range(0, 4):
#     turt.forward(100)
#     turt.right(90)

# Challenge 2

# turt.teleport(scr.canvwidth * -1, 0)

# for i in range(0,50):
#     if i % 2 != 0:
#         turt.penup()
#     else:
#         turt.pendown()
#     turt.forward(10)

# Challenge 3

# for i in range(3,11):
#     max_rgb = int(scr.colormode())
#     r = random.randint(0, max_rgb)
#     g = random.randint(0, max_rgb)
#     b = random.randint(0, max_rgb)
#
#     turt.pencolor(r, g, b)
#
#     for s in range(0,i):
#         turt.forward(100)
#         turt.right(360/i)

# Challenge 4

# turt.pensize(10)
# turt.speed('fastest')
#
# for i in range(0,200):
#     max_rgb = int(scr.colormode())
#     r = random.randint(0, max_rgb)
#     g = random.randint(0, max_rgb)
#     b = random.randint(0, max_rgb)
#
#     turt.pencolor(r, g, b)
#
#     turt.forward(20)
#
#     angle = random.randint(0,3) * 90
#     turt.setheading(angle)

# Challenge 5

# turt.pensize(10)
# turt.speed('fastest')
#
# for i in range(0,200):
#     scr.colormode(255)
#     max_rgb = int(scr.colormode())
#
#     r = random.randint(0, max_rgb)
#     g = random.randint(0, max_rgb)
#     b = random.randint(0, max_rgb)
#
#     rgb = (r, g, b)
#
#     print(rgb)
#
#     turt.pencolor(rgb)
#
#     turt.forward(20)
#
#     angle = random.randint(0,3) * 90
#     turt.setheading(angle)

# Challenge 6

turt.pensize(1)
turt.speed('fastest')

for i in range(0,90):
    scr.colormode(255)
    max_rgb = int(scr.colormode())

    r = random.randint(0, max_rgb)
    g = random.randint(0, max_rgb)
    b = random.randint(0, max_rgb)

    rgb = (r, g, b)
    turt.pencolor(rgb)

    turt.circle(100)

    turt.setheading(i * 4)




scr.exitonclick()