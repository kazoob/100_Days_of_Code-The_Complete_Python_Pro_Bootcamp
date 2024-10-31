from turtle import Turtle, Screen
import pandas
from PIL import Image

SCREEN_TITLE = "US States Game"
SCREEN_WIDTH_DEFAULT = 800
SCREEN_HEIGHT_DEFAULT = 600

STATES_CSV = "50_states.csv"
STATES_IMAGE = "blank_states_img.gif"

MISSING_STATES_CSV = "missing_states.csv"

TURTLE_FONT = ('Courier', 12, 'normal')
TURTLE_FONT_GAME_OVER = ('Courier', 24, 'normal')
TURTLE_ALIGN = "center"


def draw_state(state, x_pos, y_pos):
    turtle.teleport(x=x_pos, y=y_pos)
    turtle.write(state, align=TURTLE_ALIGN, font=TURTLE_FONT)


# Get the image size.
try:
    with Image.open(STATES_IMAGE) as img:
        screen_width, screen_height = img.size
# Image does not exist, use default screen size.
except FileNotFoundError:
    screen_width = SCREEN_WIDTH_DEFAULT
    screen_height = SCREEN_HEIGHT_DEFAULT
except Exception as e:
    print(e)
    screen_width = SCREEN_WIDTH_DEFAULT
    screen_height = SCREEN_HEIGHT_DEFAULT

# Open the CSV file.
states = pandas.read_csv(STATES_CSV)

# Set up the screen
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.title(SCREEN_TITLE)

# Set the screen background.
try:
    screen.bgpic(STATES_IMAGE)
# Image does not exist.
except Exception as e:
    print(e)

# Set up the text writing turtle.
turtle = Turtle()
turtle.hideturtle()
turtle.penup()

# Start the game.
correct_states = 0
num_states = len(states)

# Continue prompting user until they hit Cancel.
guess = ""
guesses = []  # Previous guess list
while guess is not None:
    # TODO Don't display "another" if first guess
    guess = screen.textinput(title=f"{correct_states}/{num_states} States Correct",
                             prompt="What is another state's name?")

    # Only process if not a repeated guess.
    if guess is not None and guess not in guesses:
        # Get the result from the CSV file.
        guess = guess.title()
        guess_result = states[states.state == guess]

        # If the guess is correct, draw the state on the map and increase score.
        if len(guess_result) >= 1:
            state = guess_result.state.item()
            x_pos = int(guess_result.x.item())
            y_pos = int(guess_result.y.item())
            draw_state(state, x_pos, y_pos)

            correct_states += 1
            # Append guess to previous guess list.
            guesses.append(guess)

        # Check if all states have been found.
        if correct_states >= num_states:
            # Display congratulations message.
            turtle.teleport(x=0, y=screen_height / 2 - 60)
            turtle.write(f"Congratulations!!\nYou named all {num_states} states.",
                         align=TURTLE_ALIGN, font=TURTLE_FONT_GAME_OVER)

            # End game loop.
            guess = None

# Compile a list of states not guessed.
missing_states = {
    "state": [state for state in states.state.to_list() if state not in guesses]
}

# Export a CSV containing all states not guessed.
report = pandas.DataFrame(missing_states)
report.to_csv(MISSING_STATES_CSV)

# Keep screen open until mouse click.
screen.exitonclick()
