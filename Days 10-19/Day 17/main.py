from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {game.score}/{game.question_number}")
