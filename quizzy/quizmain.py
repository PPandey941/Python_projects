from question_model import Questions
from quizdata import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    new_q = Questions(i["question"], i["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your score is {quiz.score}/{quiz.question_number}")