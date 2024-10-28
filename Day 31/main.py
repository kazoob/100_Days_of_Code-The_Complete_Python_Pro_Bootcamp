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

LANGUAGE_TEXT_Y_OFFSET = 113
LANGUAGE_TEXT_FONT = ("Arial", 40, "italic")
WORD_TEXT_FONT = ("Arial", 60, "bold")

FLASH_CARD_TIME = 3000


def right():
    if is_flash_card_back():
        # Remove word from word list
        word_list.remove(current_word)

        # Display new flash card
        new_flash_card()


def wrong():
    if is_flash_card_back():
        # TODO add to incorrect word list?

        # Display new flash card
        new_flash_card()


def new_word():
    # Check if there are words left in the word list
    if len(word_list) > 0:
        # Return new word
        return random.choice(word_list)
    else:
        return None


def display_flash_card_front():
    flash_card.itemconfig(flash_card_image, image=flash_card_front_img)


def display_flash_card_back():
    flash_card.itemconfig(flash_card_image, image=flash_card_back_img)


def new_flash_card():
    global current_word

    current_word = new_word()

    if current_word is not None:
        update_flash_card(current_word, lang_a)
    else:
        display_flash_card_front()
        # TODO end of word list


def update_flash_card(word, lang):
    # Learning language
    if lang == lang_a:
        # Display flash card front
        display_flash_card_front()

        # Schedule flash card back (answer)
        window.after(FLASH_CARD_TIME, update_flash_card, word, lang_b)
    # Solution language
    else:
        # Display flash card back (answer)
        display_flash_card_back()

    # Update language text
    flash_card.itemconfig(flash_card_language, text=lang)

    # Update word text
    flash_card.itemconfig(flash_card_word, text=word.get(lang))


def is_flash_card_back():
    # Get current card PhotoImage string
    current_card = flash_card.itemcget(flash_card_image, "image")

    # Get back card PhotoImage string
    back_card = str(flash_card_back_img)

    # Return back card status
    return current_card == back_card


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
flash_card_x = flash_card_width / 2
flash_card_y = flash_card_height / 2

flash_card = Canvas(width=flash_card_width, height=flash_card_height, bg=WINDOW_BG_COLOR, highlightthickness=0)
flash_card_image = flash_card.create_image(flash_card_x, flash_card_y)
flash_card_language = flash_card.create_text(flash_card_x, flash_card_y - LANGUAGE_TEXT_Y_OFFSET,
                                             font=LANGUAGE_TEXT_FONT)
flash_card_word = flash_card.create_text(flash_card_x, flash_card_y, font=WORD_TEXT_FONT)
flash_card.grid(column=0, row=0, columnspan=2)

# Create the buttons
# TODO try except
right_img = PhotoImage(file=IMAGE_RIGHT)
# TODO remove border
right_button = Button(image=right_img, command=right, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)

# TODO try except
wrong_img = PhotoImage(file=IMAGE_WRONG)
# TODO remove border
wrong_button = Button(image=wrong_img, command=wrong, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

# Load the word data
# TODO try except
with open(WORD_LIST) as file:
    word_data = pandas.read_csv(file)

# Create the word list dictionary
word_list = word_data.to_dict(orient="records")

# Get the learning and solution languages from the data frame
lang_a = word_data.columns[0]
lang_b = word_data.columns[1]

# Display the first flash card
current_word = {}
new_flash_card()

# Keep the window on the screen.
window.mainloop()
