from turtle import Turtle, Screen

scr = Screen()
# rootwindow = scr.getcanvas().winfo_toplevel()
# rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
# rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

turt = Turtle()
turt.shape("turtle")
turt.color("orange")

turt.teleport(scr.canvwidth * -1, 0)

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

# for i in range(0,50):
#     if i % 2 != 0:
#         turt.penup()
#     else:
#         turt.pendown()
#     turt.forward(10)

# Challenge 3






scr.exitonclick()