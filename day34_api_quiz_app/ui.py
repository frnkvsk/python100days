from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.question = ""
        self.label_score = Label(
            text=f"Score: {self.score}",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 16, 'italic')
        )
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text=self.question,
            fill=THEME_COLOR,
            font=("Arial", 20, 'italic'),
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=next_question)
        else:
            self.canvas.itemconfig(self.text_question, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, correct: bool):
        if correct:
            self.canvas.config(bg="green")
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)