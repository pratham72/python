from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_ques = Question(text, answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you have completed the quiz.")
print(f"you final score was: {quiz.score}/{quiz.question_number}.")