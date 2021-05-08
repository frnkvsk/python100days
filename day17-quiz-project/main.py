from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
   next_question = Question(x['question'], x['correct_answer'])
   question_bank.append(next_question)
   
quiz = QuizBrain(question_bank)
while quiz.has_next():
   user_input = quiz.next_question()

quiz.print_final_score()