
class QuizBrain:
   def __init__(self, q_list):
      self.question_number = 0
      self.score = 0
      self.question_list = q_list

   def next_question(self):
      current_question = self.question_list[self.question_number]
      user_input = input(f"Q.{self.question_number}: {current_question.question} ")
      self.check_answer(user_input, current_question.answer)
      self.question_number += 1

   def has_next(self):
      return self.question_number < len(self.question_list)

   def check_answer(self, user_input, correct_answer):
      if user_input.lower() == correct_answer.lower():
         print('You got it right!')
         self.score += 1
      else:
         print("That's wrong.")
      print(f"The correct answer was: {correct_answer}")
      print(f"Your current score is: {self.score}/{self.question_number+1}")
      print("\n")

   def print_final_score(self):
      print("""
      You've completed the quiz
      Your final score was: {0}/{1}
      """.format(self.score, self.question_number))