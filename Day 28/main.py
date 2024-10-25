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
STATUS_LONG_BREAK = "Break"

# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2

# ---------------------------- TIMER RESET ------------------------------- #
cycle = 0  # Current work / break cycle
# Odd = Work
# Even = Break
# Multiple of 8 = Long break
timer_seconds = 0  # Timer seconds remaining

# TODO Replace with window.after_cancel()
timer_running = False


def timer_reset():
    """Stop the timer. Reset the current cycle."""
    global cycle
    global timer_running

    # Stop timer
    timer_running = False

    # Reset the current cycle
    timer_set()
    timer_update()

    # Move cycle back so that timer_start() moves it forward again.
    # TODO could do this better
    if cycle > 0:
        cycle -= 1


def timer_set():
    """Set the timer and the current cycle label."""
    global timer_seconds

    # Timer is idle
    if cycle == 0:
        status_label.config(text=STATUS_IDLE, fg=GREEN)

    # Long break cycle
    elif cycle % 8 == 0:
        timer_seconds = int(LONG_BREAK_MIN * 60)
        status_label.config(text=STATUS_LONG_BREAK, fg=RED)

    # Short break cycle
    elif cycle % 2 == 0:
        timer_seconds = int(SHORT_BREAK_MIN * 60)
        status_label.config(text=STATUS_BREAK, fg=PINK)

    # Work cycle
    else:
        timer_seconds = int(WORK_MIN * 60)
        status_label.config(text=STATUS_WORK, fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
    """Start the timer."""
    global cycle
    global timer_running

    # Only start the timer if it is not already running
    if not timer_running:
        # Advance the current cycle.
        # TODO could do this better
        cycle += 1

        # Set the timer
        timer_set()

        # Start the timer
        timer_running = True
        timer_update()

        # Schedule 1 second updates
        window.after(1000, timer_countdown)


def timer_update():
    """Update the timer countdown."""
    # Timer is idle
    if cycle == 0:
        timer_string = "--:--"

    # Timer is running
    else:
        timer_string = f"{timer_seconds // 60:02d}:{timer_seconds % 60:02d}"

    # Update the label
    tomato_canvas.itemconfig(timer_text, text=timer_string)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_countdown():
    """Countdown the timer 1 second. If a work cycle has been completed, add a check mark."""
    global cycle
    global timer_seconds
    global timer_running

    # Only proceed if timer is supposed to be running.
    if timer_running:
        # Timer still has time remaining, count down.
        if timer_seconds > 0:
            timer_seconds -= 1
            timer_update()
            window.after(1000, timer_countdown)

        # TImer has completed.
        else:
            # Update check marks if work cycle completed.
            if cycle % 2 == 1:
                new_checks = status_checks.cget("text") + CHECK_SYMBOL
                status_checks.config(text=new_checks)

            # Stop the timer
            timer_running = False

            # Start the timer with the next cycle.
            timer_start()


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
timer_text = tomato_canvas.create_text(tomato_img_width / 2, tomato_img_height / 2 + 18, fill="white",
                                       font=(FONT_NAME, FONT_SIZE_TIMER, "bold"))
tomato_canvas.grid(column=1, row=1)

# Create the labels
status_label = Label(text=STATUS_IDLE, font=(FONT_NAME, FONT_SIZE_STATUS), bg=YELLOW, fg=GREEN)
status_label.grid(column=1, row=0)

status_checks = Label(font=(FONT_NAME, FONT_SIZE_CHECK), bg=YELLOW, fg=GREEN)
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
