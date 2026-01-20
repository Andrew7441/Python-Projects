from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    newQuestion  = Question(question["text"], question["answer"])
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()


print("Quiz complete!")
print(f"Final Score: {quiz.score}/{len(question_bank)}")
