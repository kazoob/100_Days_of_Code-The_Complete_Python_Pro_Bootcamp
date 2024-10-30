from tkinter import *

THEME_COLOR = "#375362"
GRID_PADDING = (20, 20)

TRUE_BUTTON_IMAGE_FILE = "images/true.png"
FALSE_BUTTON_IMAGE_FILE = "images/false.png"

QUESTION_WIDTH = 300
QUESTION_HEIGHT = 250
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self):
        self.score = 0

        # Set up the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        # Set up the label
        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=GRID_PADDING, pady=GRID_PADDING)
        self.update_score()

        # Set up the canvas
        self.question_canvas = Canvas(width=QUESTION_WIDTH, height=QUESTION_HEIGHT, bg="white", highlightthickness=0)
        self.question_field = self.question_canvas.create_text(QUESTION_WIDTH / 2, QUESTION_HEIGHT / 2,
                                                               fill=THEME_COLOR, font=QUESTION_FONT, text="Question")
        self.question_canvas.grid(column=0, row=1, columnspan=2, padx=GRID_PADDING, pady=GRID_PADDING)

        # Set up the buttons
        self.true_button_img = PhotoImage(file=TRUE_BUTTON_IMAGE_FILE)
        self.true_button = Button(image=self.true_button_img)
        self.true_button.grid(column=0, row=2, padx=GRID_PADDING, pady=GRID_PADDING)

        self.false_button_img = PhotoImage(file=FALSE_BUTTON_IMAGE_FILE)
        self.false_button = Button(image=self.false_button_img)
        self.false_button.grid(column=1, row=2, padx=GRID_PADDING, pady=GRID_PADDING)

        # Keep the window open
        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
