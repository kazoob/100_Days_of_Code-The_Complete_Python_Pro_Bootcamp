from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WINDOW_PADDING_X = 50
WINDOW_PADDING_Y = 50

LOGO_IMAGE = "logo.png"
LOGO_PADDING = 1

USERNAME_FILE_NAME = "username.txt"
PASSWORD_FILE_NAME = "passwords.json"


def generate_password():
    """Generate a random password. Copy to the clipboard. Code from Day 5."""
    # Library of letters, numbers and symbols.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Empty password list
    password_list = []

    # Populate password list with random letters, symbols and numbers
    password_list.extend([random.choice(letters) for _ in range(random.randint(8, 10))])
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    # Shuffle the password list
    random.shuffle(password_list)

    # Convert the password list to a password string
    password = "".join(password_list)

    # Replace password input with generated password string
    password_input.delete(0, END)
    password_input.insert(END, password)

    # Copy the password string to the clipboard
    pyperclip.copy(password)


def save_password():
    """Save the password to the database. Ensure that all fields are valid."""
    # Get the input data
    website = website_input.get().strip()
    username = username_input.get().strip()
    password = password_input.get().strip()

    # Make sure all input fields have data
    if website and username and password:
        # Create the password dictionary
        data = {
            website: {
                "username": username,
                "password": password,
            }
        }

        # Add the password to the password database
        passwords.update(data)

        # Write the password database to disk
        with open(PASSWORD_FILE_NAME, mode="w") as password_file_w:
            json.dump(passwords, password_file_w, indent=4)

        # Save username to text file, to be re-used when application is opened
        with open(USERNAME_FILE_NAME, mode="w") as username_file_rw:
            username_file_rw.write(username)

        # Clear the fields
        website_input.delete(0, END)
        password_input.delete(0, END)
    else:
        messagebox.showerror(title="Invalid Data", message="Some of the fields are empty.")


def search_password():
    # Get the input data
    website = website_input.get().strip()

    # Verify that the website is not empty
    if website:
        # Try to get the entry in the password database
        try:
            # Get the username and password
            username = passwords[website]["username"]
            password = passwords[website]["password"]
        # The password does not exist, display error message and clear input box
        except KeyError:
            messagebox.showinfo(title="Website Not Found", message=f"Website '{website}' was not found.")
            website_input.delete(0, END)
        # The password was found in the password database
        else:
            # Populate the username field
            username_input.delete(0, END)
            username_input.insert(END, username)

            # Populate the password field
            password_input.delete(0, END)
            password_input.insert(END, password)


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
website_input = Entry(width=23)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=23)
password_input.grid(column=1, row=3)

# Create the buttons
generate_pw_button = Button(text="Generate Password", width=13, command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_pw_button = Button(text="Add", width=37, command=save_password)
add_pw_button.grid(column=1, row=4, columnspan=2)

search_pw_button = Button(text="Search", width=13, command=search_password)
search_pw_button.grid(column=2, row=1)

# Restore previous username (if found)
try:
    with open(USERNAME_FILE_NAME, mode="r") as username_file_r:
        username_prev = username_file_r.read().strip()
        username_input.insert(END, string=username_prev)
except FileNotFoundError as e:
    print(e)

# Read existing password database (if found)
try:
    with open(PASSWORD_FILE_NAME, mode="r") as password_file_r:
        passwords = json.load(password_file_r)
except FileNotFoundError as e:
    # Create empty password database
    passwords = {}
    print(e)

# Keep window open
window.mainloop()
