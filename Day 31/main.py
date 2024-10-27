from tkinter import *
import pandas
import random

WORD_LIST = "data/french_words.csv"

WINDOW_BG_COLOR = "#B1DDC6"
WINDOW_PADDING = 50

IMAGE_RIGHT = "images/right.png"
IMAGE_WRONG = "images/wrong.png"
IMAGE_FLASH_FRONT = "images/card_front.png"
IMAGE_FLASH_BACK = "images/card_back.png"

LANGUAGE_TEXT_X = 400
LANGUAGE_TEXT_Y = 150
LANGUAGE_TEXT_FONT = ("Arial", 40, "italic")

WORD_TEXT_X = 400
WORD_TEXT_Y = 263
WORD_TEXT_FONT = ("Arial", 60, "bold")


def right():
    pass


def wrong():
    pass


# Set up the window.
window = Tk()
window.title("Flashy")
window.config(bg=WINDOW_BG_COLOR, padx=WINDOW_PADDING, pady=WINDOW_PADDING)

# Create the canvas
# TODO try except
flash_card_front_img = PhotoImage(file=IMAGE_FLASH_FRONT)
flash_card_back_img = PhotoImage(file=IMAGE_FLASH_BACK)

flash_card_width = flash_card_front_img.width()
flash_card_height = flash_card_front_img.height()

flash_card = Canvas(width=flash_card_width, height=flash_card_height, bg=WINDOW_BG_COLOR, highlightthickness=0)
flash_card.create_image(flash_card_width / 2, flash_card_height / 2, image=flash_card_front_img)
language_text = flash_card.create_text(LANGUAGE_TEXT_X, LANGUAGE_TEXT_Y, font=LANGUAGE_TEXT_FONT)
word_text = flash_card.create_text(WORD_TEXT_X, WORD_TEXT_Y, font=WORD_TEXT_FONT)
flash_card.grid(column=0, row=0, columnspan=2)

# Create the buttons
# TODO try except
right_img = PhotoImage(file=IMAGE_RIGHT)
# TODO remove border
right_button = Button(image=right_img, command=right, highlightthickness=0)
right_button.grid(column=1, row=1)

# TODO try except
wrong_img = PhotoImage(file=IMAGE_WRONG)
# TODO remove border
wrong_button = Button(image=wrong_img, command=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Load the words
# TODO try except
with open(WORD_LIST) as file:
    word_list = pandas.read_csv(file).to_dict(orient="records")

# Display the first flash card
word = random.choice(word_list)
print(word)
flash_card.itemconfig(language_text, text="French")
flash_card.itemconfig(word_text, text="hot dog")

# Keep the window on the screen.
window.mainloop()
