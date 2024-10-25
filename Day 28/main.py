from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
WINDOW_PADDING_X = 100
WINDOW_PADDING_Y = 50
WINDOW_IMAGE = "tomato.png"

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE_STATUS = 50
FONT_SIZE_TIMER = 35
FONT_SIZE_BUTTON = 16
FONT_SIZE_CHECK = 26

CHECK_SYMBOL = "✔"
STATUS_IDLE = "----"
STATUS_WORK = "Work"
STATUS_BREAK = "Break"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
timer_min = 0
timer_sec = 0
timer_running = False


def timer_reset():
    global timer_min
    global timer_sec
    global timer_running

    timer_min = WORK_MIN
    timer_sec = 0
    timer_running = False
    status_label.config(text=STATUS_IDLE)

    timer_update()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    global timer_running

    timer_running = True
    status_label.config(text=STATUS_WORK)

    window.after(1000, timer_countdown)


def timer_update():
    tomato_canvas.itemconfig(timer_text, text=f"{timer_min:02d}:{timer_sec:02d}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_countdown():
    if timer_running:
        global timer_min
        global timer_sec

        if timer_sec > 0:
            timer_sec -= 1
        elif timer_min > 0:
            timer_min -= 1
            timer_sec = 59
        else:
            # TODO
            pass

        timer_update()
        window.after(1000, timer_countdown)


# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y)
window.config(bg=YELLOW)

# Open the image
tomato_img = PhotoImage(file=WINDOW_IMAGE)

# Get the image size
tomato_img_width = tomato_img.width()
tomato_img_height = tomato_img.height()

# Create the image and timer canvas
tomato_canvas = Canvas(width=tomato_img_width + 2, height=tomato_img_height + 2, bg=YELLOW, highlightthickness=0)
tomato_canvas.create_image(tomato_img_width / 2 + 1, tomato_img_height / 2 + 1, image=tomato_img)
timer_text = tomato_canvas.create_text(tomato_img_width / 2, tomato_img_height / 2 + 18, text="", fill="white",
                                       font=(FONT_NAME, FONT_SIZE_TIMER, "bold"))
tomato_canvas.grid(column=1, row=1)

# Create the labels
status_label = Label(text=STATUS_IDLE, font=(FONT_NAME, FONT_SIZE_STATUS), bg=YELLOW, fg=GREEN)
status_label.grid(column=1, row=0)

status_checks = Label(text="", font=(FONT_NAME, FONT_SIZE_CHECK), bg=YELLOW, fg=GREEN)
status_checks.grid(column=1, row=3)

# Create the buttons
start_button = Button(text="Start", command=timer_start, font=(FONT_NAME, FONT_SIZE_BUTTON), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=timer_reset, font=(FONT_NAME, FONT_SIZE_BUTTON), highlightthickness=0)
reset_button.grid(column=2, row=2)

# Reset the timer
timer_reset()

# Keep window open
window.mainloop()
