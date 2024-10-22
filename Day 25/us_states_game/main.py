from turtle import Turtle, Screen
import pandas
from PIL import Image

SCREEN_TITLE = "US States Game"
SCREEN_WIDTH_DEFAULT = 800
SCREEN_HEIGHT_DEFAULT = 600

STATES_CSV = "50_states.csv"
STATES_IMAGE = "blank_states_img.gif"

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

# Keep screen open until mouse click.
screen.exitonclick()
