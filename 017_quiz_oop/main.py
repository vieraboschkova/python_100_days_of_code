from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
questions = []

for question in question_data:
    question_text = question["text"]
    question_correct_answer = question["answer"]
    new_question = Question(question_text, question_correct_answer)
    questions.append(new_question)

# print(questions)

my_brain = QuizBrain(questions)
while my_brain.has_more_questions():
    my_brain.ask_next_question()

# class User:
#     def __init__(self, name = "unknown"):
#         self.name = name
#         self.followers = 0
#         self.following = []
    
#     def follow(self, user):
#         user.followers += 1
#         self.following.append(user.name)

# user_1 = User('a')
# user_2 = User('b')
# user_2.follow(user_1)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)