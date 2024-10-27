from tkinter import *

WINDOW_BG_COLOR = "#B1DDC6"
WINDOW_PADDING = 50

IMAGE_RIGHT = "images/right.png"
IMAGE_WRONG = "images/wrong.png"
IMAGE_FLASH_FRONT = "images/card_front.png"
IMAGE_FLASH_BACK = "images/card_back.png"


def right():
    pass


def wrong():
    pass


# Set up the window.
window = Tk()
window.title = "Flashy"
window.config(bg=WINDOW_BG_COLOR, padx=WINDOW_PADDING, pady=WINDOW_PADDING)

# Create the canvas
# TODO try except
flash_card_front_img = PhotoImage(file=IMAGE_FLASH_FRONT)
flash_card_back_img = PhotoImage(file=IMAGE_FLASH_BACK)

flash_card_width = flash_card_front_img.width()
flash_card_height = flash_card_front_img.height()

flash_card = Canvas(width=flash_card_width, height=flash_card_height, bg=WINDOW_BG_COLOR, highlightthickness=0)
flash_card.create_image(flash_card_width / 2, flash_card_height / 2, image=flash_card_front_img)
flash_card.grid(column=0, row=0, columnspan=2)

# Create the buttons
# TODO try except
right_img = PhotoImage(file=IMAGE_RIGHT)
right_button = Button(image=right_img, command=right, highlightthickness=0)
right_button.grid(column=1, row=1)

# TODO try except
wrong_img = PhotoImage(file=IMAGE_WRONG)
wrong_button = Button(image=wrong_img, command=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Keep the window on the screen.
window.mainloop()
