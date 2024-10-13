from turtle import Turtle, Screen
import random

# List of colors for each turtle.
TURTLE_COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
]

# Screen size.
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

# Start and finish line offset.
LINE_OFFSET = 40

# Turtle movement parameters.
MOVE_MIN = 1
MOVE_MAX = 10

# List of turtles in the race.
turtles = []

# Start and finish line positions.
START_X = (-1 * SCREEN_WIDTH / 2) + LINE_OFFSET
END_X = (SCREEN_WIDTH / 2) - LINE_OFFSET


def race_setup():
    """Set up the race. Draws the start and finish lines. Place each turtle at the start line."""
    # Draw the start and finish lines.
    setup_turtle = Turtle()
    setup_turtle.speed("fastest")

    # Disable screen updates.
    scr.tracer(0)
    # Start line.
    setup_turtle.teleport(x=START_X, y=SCREEN_HEIGHT / 2)
    setup_turtle.setheading(270)
    setup_turtle.forward(SCREEN_HEIGHT)
    # Finish line.
    setup_turtle.teleport(x=END_X, y=SCREEN_HEIGHT / 2)
    setup_turtle.forward(SCREEN_HEIGHT)
    # Enable screen updates.
    scr.tracer(1)

    # Create and place each turtle.
    for i in range(0, len(TURTLE_COLORS)):
        turtle = Turtle(shape="turtle")
        turtle.color(TURTLE_COLORS[i])
        turtle.penup()
        turtle.speed("fastest")
        # Place turtle at the start line.
        turtle_x = START_X - 18
        turtle_y = (SCREEN_HEIGHT / 2) - (i + 1) * 40
        turtle.teleport(x=turtle_x, y=turtle_y)

        # Add turtle to list of turtles in the race.
        turtles.append(turtle)


def move_turtles():
    """Randomly move each turtle one iteration, between MOVE_MIN and MOVE_MAX."""
    for i in range(0, len(turtles)):
        turtles[i].forward(random.randint(MOVE_MIN, MOVE_MAX))


def get_winner():
    """Check if there is a winner. If yes, returns the color name, If no, returns None."""
    winner_color = None
    winner_pos = 0

    # Iterate through each turtle.
    for turtle in turtles:
        turtle_col = turtle.color()[0]
        turtle_x = turtle.xcor()

        # Check if turtle has passed the finish line.
        if turtle_x > END_X - 18:
            # Check if turtle is farther than the previous turtle passed the finish line.
            if turtle_x > winner_pos:
                winner_color = turtle_col
                winner_pos = turtle_x

    return winner_color


# Set up the screen.
scr = Screen()
scr.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
scr.colormode(255)
scr.bgcolor("gray40")

# Set up the race.
race_setup()

# Compile list of colors for player prompt.
colors = ""
for color in TURTLE_COLORS:
    if colors != "":
        colors += "/"
    colors += color

# Get bet from player.
bet = ""
while bet not in TURTLE_COLORS:
    bet = scr.textinput(title="Place a bet", prompt=f"Which turtle will win the race? Enter a color ({colors}): ")

# Keep moving race forward until there is a winner.
winner = None
while winner is None:
    move_turtles()
    winner = get_winner()

# Output results.
print(f"Bet: {bet}")
print(f"Winner: {winner}")

if bet == winner:
    print("You win!")
else:
    print("You lose.")

# Keep screen open until mouse click.
scr.exitonclick()
