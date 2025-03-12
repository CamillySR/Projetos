from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for look in question_data:
    current_question = look["question"]
    current_answer = look["correct_answer"]
    new_question = Question(current_question, current_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)



while quiz.still_has_questions():
    quiz.next_question()

