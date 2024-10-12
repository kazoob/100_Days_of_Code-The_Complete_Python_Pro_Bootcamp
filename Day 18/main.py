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

for i in range(3,11):
    max_rgb = int(scr.colormode())
    r = random.randint(0, max_rgb)
    g = random.randint(0, max_rgb)
    b = random.randint(0, max_rgb)

    turt.pencolor(r, g, b)

    for s in range(0,i):
        turt.forward(100)
        turt.right(360/i)





scr.exitonclick()