from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_number = 0

question_bank = []

for i in question_data:
    current_question = Question(i['text'], i['answer'])
    question_number += 1
    question_bank.append(current_question)
print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
