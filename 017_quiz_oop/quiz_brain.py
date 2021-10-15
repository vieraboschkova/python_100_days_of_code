class QuizBrain:


    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def has_more_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, correct_answer, user_answer):
        return correct_answer.lower() == user_answer.lower()

    def ask_next_question(self):
        player_answer = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text}: (True/False) ")
        if player_answer == "end":
            self.question_number = len(self.questions_list) - 1
        elif self.check_answer(self.questions_list[self.question_number].answer, player_answer):
            self.score += 1
            print(f"Correct! Your score is {self.score}")
            print("\n")
        else:
            print(f"Wrong! Your score is {self.score}")
            print("\n")
        self.question_number += 1
        if self.question_number > len(self.questions_list) - 1:
            print("End of quiz! No more quesitons!")
