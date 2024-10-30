from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WINDOW_PADDING = 20
GRID_PADDING_Y = 50
BUTTON_PADDING_X = 20

TRUE_BUTTON_IMAGE_FILE = "images/true.png"
FALSE_BUTTON_IMAGE_FILE = "images/false.png"

QUESTION_WIDTH = 300
QUESTION_HEIGHT = 250
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        # Set up the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=WINDOW_PADDING, pady=WINDOW_PADDING)

        # Set up the label
        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.update_score()

        # Set up the canvas
        self.question_canvas = Canvas(width=QUESTION_WIDTH, height=QUESTION_HEIGHT, bg="white", highlightthickness=0)
        self.question_field = self.question_canvas.create_text(QUESTION_WIDTH / 2, QUESTION_HEIGHT / 2,
                                                               fill=THEME_COLOR, font=QUESTION_FONT,
                                                               width=QUESTION_WIDTH - 20)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=GRID_PADDING_Y)

        # Set up the buttons
        true_button_img = PhotoImage(file=TRUE_BUTTON_IMAGE_FILE)
        self.true_button = Button(image=true_button_img, highlightthickness=0, bd=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2, padx=BUTTON_PADDING_X)

        false_button_img = PhotoImage(file=FALSE_BUTTON_IMAGE_FILE)
        self.false_button = Button(image=false_button_img, highlightthickness=0, bd=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=BUTTON_PADDING_X)

        # Display first question
        self.get_next_question()

        # Keep the window open
        self.window.mainloop()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def get_next_question(self):
        question = self.quiz.next_question()
        self.question_canvas.itemconfig(self.question_field, text=question)

    def answer_true(self):
        self.quiz.check_answer("true")
        self.get_next_question()

    def answer_false(self):
        self.quiz.check_answer("false")
        self.get_next_question()
