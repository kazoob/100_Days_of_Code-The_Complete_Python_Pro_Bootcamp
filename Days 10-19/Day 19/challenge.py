from turtle import Turtle, Screen

def move_forward():
    turt.forward(10)

def move_backward():
    turt.backward(10)

def move_left():
    turt.left(10)

def move_right():
    turt.right(10)

def clear_screen():
    turt.clear()
    turt.teleport(x=0, y=0)

turt = Turtle()
turt.color("orange")
turt.speed("fastest")

scr = Screen()

scr.listen()
scr.onkeypress(key="w", fun=move_forward)
scr.onkeypress(key="s", fun=move_backward)
scr.onkeypress(key="a", fun=move_left)
scr.onkeypress(key="d", fun=move_right)
scr.onkeypress(key="c", fun=clear_screen)

scr.exitonclick()