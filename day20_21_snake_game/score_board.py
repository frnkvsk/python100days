from turtle import Turtle


class Score(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.width = width
        self.height = height
        self.score = 0
        self.goto(-10, self.height / 2 - 17)
        self.color('white')
        self.hideturtle()
        self.display_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:  {self.score}", False, align='center', font=("Arial", 16, "normal"))

    def display_score(self):
        self.write(f"Score:  {self.score}", False, align='center', font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align='center', font=("Arial", 12, "normal"))

