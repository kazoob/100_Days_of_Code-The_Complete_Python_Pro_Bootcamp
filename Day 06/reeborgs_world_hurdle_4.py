def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    wall = 0
    while wall_on_right():
        move()
        wall += 1
    turn_right()
    move()
    turn_right()
    for x in range(0, wall):
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
