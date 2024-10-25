from tkinter import *

WINDOW_WIDTH = 260
WINDOW_HEIGHT = 130
WINDOW_PADDING = 20

DEFAULT_VALUE = 1


def calculate():
    """Get the user input and convert to miles. Display result. If input is not a number, display 'error'."""
    try:
        # Convert input to int and convert to km
        result = int(user_input.get()) * 1.609
    except ValueError:
        result = "error"
    except Exception as e:
        result = "error"
        print(e)

    # Update the result
    label_result.config(text=result)

    # Return focus to input box
    user_input.focus()


# Create window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING)

# Create input box
user_input = Entry(width=10)
user_input.insert(END, string=f"{DEFAULT_VALUE}")
user_input.grid(column=1, row=0)

# Create labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="")
label_result.grid(column=1, row=1)

# Create button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# Calculate the initial result
calculate()

# Keep window on screen
window.mainloop()
