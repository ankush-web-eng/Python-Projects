class Quizbrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question (self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.correct_answer(user_answer, current_question.answer)

    def correct_answer(self, user_answer, cor_answer):
        if user_answer.lower() == cor_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("OOPS! That was Wrong!!")
            print(f"Your answer was {user_answer}")
            print(f"Correct Answer was {cor_answer}")
        print(f"Your Current Score is {self.score}/{self.question_number}")
        print("\n")
        