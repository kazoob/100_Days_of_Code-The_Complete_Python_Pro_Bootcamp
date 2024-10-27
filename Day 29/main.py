from tkinter import *

WINDOW_PADDING_X = 20
WINDOW_PADDING_Y = 20

LOGO_IMAGE = "logo.png"
LOGO_PADDING = 1

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass

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
logo_canvas_width = logo_img_width + LOGO_PADDING * 2
logo_canvas_height = logo_img_height + LOGO_PADDING * 2
logo_canvas = Canvas(width=logo_canvas_width, height=logo_canvas_height, highlightthickness=0)

logo_canvas_img_x = logo_img_width / 2 + LOGO_PADDING
logo_canvas_img_y = logo_img_width / 2 + LOGO_PADDING
logo_canvas.create_image(logo_canvas_img_x, logo_canvas_img_y, image=logo_img)

logo_canvas.grid(column=1, row=0)

# Create the labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="E-mail / Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create the inputs
website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# Create the buttons
generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_pw_button = Button(text="Add", width=37, command=save_password)
add_pw_button.grid(column=1, row=4, columnspan=2)

# Keep window open
window.mainloop()