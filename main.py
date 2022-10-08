from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUi

try:
    from data import question_data

    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


except ImportError:
    pass

except ConnectionError:
    print("yes")
else:
    if len(question_data) != 0:
        quiz = QuizBrain(question_bank)
        quiz_ui = QuizUi(quiz)
