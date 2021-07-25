class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}: {current_question.text} (True/False):")




# question_number = 0
#
# for i in question_bank:
#     question_number += 1
#     user_choice = input(f"Q{question_number}:  Choose 'True' or 'False'. {i.text}// answer is {i.answer}")
#
#     if user_choice == i.answer:
#         print("Good Job. Next Question")
#
#     else:
#         print("Your answer is incorrect, try again next time.")

