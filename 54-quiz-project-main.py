from data import question_data
from qsmodel import Question
from quiz_brain import QuizBrain

question_bank = []

for n in question_data:
    question_text = n["text"]
    question_answer = n["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_question():
 quiz.next_question()

print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")