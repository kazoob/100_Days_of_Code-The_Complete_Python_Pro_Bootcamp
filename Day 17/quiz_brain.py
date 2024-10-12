class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {question.question} (True/False)?: ").lower()
        self.check_answer(answer, question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer is {question_answer}.\n")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
