from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_text)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You Completed the Quiz!!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
