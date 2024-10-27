from tkinter import *

WINDOW_PADDING_X = 20
WINDOW_PADDING_Y = 20

LOGO_IMAGE = "logo.png"
LOGO_PADDING = 1

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("Password Manager")
window.config(padx=WINDOW_PADDING_X, pady=WINDOW_PADDING_Y)

# Open the logo
logo_img = PhotoImage(file=LOGO_IMAGE)

# Get the logo image size
logo_img_width = logo_img.width()
logo_img_height = logo_img.height()

# Create the logo canvas
logo_canvas = Canvas(width=logo_img_width + LOGO_PADDING * 2, height=logo_img_height + LOGO_PADDING * 2, highlightthickness=0)
logo_canvas.create_image(logo_img_width / 2 + LOGO_PADDING, logo_img_width / 2 + LOGO_PADDING, image=logo_img)
logo_canvas.grid(column=1, row=1)

# Keep window open
window.mainloop()
