from tkinter import *

WINDOW_PADDING_X = 50
WINDOW_PADDING_Y = 50

LOGO_IMAGE = "logo.png"
LOGO_PADDING = 1

USERNAME_FILE_NAME = "username.txt"
PASSWORD_FILE_NAME = "passwords.txt"
PASSWORD_SEPARATOR = "|"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Make sure all input fields have data
    if website != "" and username != "" and password != "":
        # Append the password to the text file
        with open(PASSWORD_FILE_NAME, mode="a") as password_file_a:
            password_file_a.write(f"{website} {PASSWORD_SEPARATOR} {username} {PASSWORD_SEPARATOR} {password}\n")

        # Save username to text file, to be re-used when application is opened
        with open(USERNAME_FILE_NAME, mode="w") as username_file_rw:
            username_file_rw.write(username)
    else:
        # TODO input validation error
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

# Restore previous username (if found)
try:
    with open(USERNAME_FILE_NAME, mode="r") as username_file_r:
        username_prev = username_file_r.read().strip()
        username_input.insert(END, string=username_prev)
except FileNotFoundError as e:
    print(e)

# Keep window open
window.mainloop()
