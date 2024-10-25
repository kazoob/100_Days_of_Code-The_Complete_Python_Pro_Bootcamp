from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# WINDOW_WIDTH = 500
# WINDOW_HEIGHT = 500
WINDOW_PADDING_X = 100
WINDOW_PADDING_Y = 50
WINDOW_IMAGE = "tomato.png"

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE_STATUS = 42
FONT_SIZE_TIMER = 30
FONT_SIZE_BUTTON = 18
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("Pomodoro Timer")
# window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y)
window.config(bg=YELLOW)

# Open the image
tomato_img = PhotoImage(file=WINDOW_IMAGE)

# Get the image size
tomato_img_width = tomato_img.width()
tomato_img_height = tomato_img.height()

# Create the image and timer canvas
tomato_canvas = Canvas(width=tomato_img_width, height=tomato_img_height, bg=YELLOW, highlightthickness=0)
tomato_canvas.create_image(tomato_img_width / 2, tomato_img_height / 2, image=tomato_img)
tomato_canvas.create_text(tomato_img_width / 2, tomato_img_height / 2 + 18, text="00:00", fill="white",
                          font=(FONT_NAME, FONT_SIZE_TIMER, "bold"))
tomato_canvas.grid(column=1, row=1)

# Create the labels
status_label = Label(text="Work", font=(FONT_NAME, FONT_SIZE_STATUS), bg=YELLOW)
status_label.grid(column=1, row=0)

# Create the buttons
start_button = Button(text="Start", font=(FONT_NAME, FONT_SIZE_BUTTON))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, FONT_SIZE_BUTTON))
reset_button.grid(column=2, row=2)

window.mainloop()
