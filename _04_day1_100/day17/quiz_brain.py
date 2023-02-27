class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.question_num = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.questions)

    def next_question(self):
        response = input(f"Q.{self.question_num+1}: {self.questions[self.question_num].text} (True/False)?: ")
        self.check_answer(response, self.questions[self.question_num].answer)
        self.question_num += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You  got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num+1}")
        print("\n")
