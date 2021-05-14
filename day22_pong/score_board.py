from turtle import Turtle
from draw_number import DrawScore


class Score(Turtle):

    def __init__(self, width, height, player_1_score, player_2_score):
        super().__init__()
        self.penup()
        self.width = width
        self.height = height
        self.score1 = player_1_score
        self.score2 = player_2_score
        self.goto(-10, self.height / 2 - 17)
        self.color('white')
        self.hideturtle()
        self.display_score()

    def update_score_1(self):
        self.score1 += 1
        self.clear()
        self.write(f"{self.score1}         {self.score2}", False, align='center', font=("Arial", 56, "normal"))

    def update_score_2(self):
        self.score2 += 1
        self.clear()
        self.write(f"{self.score1}         {self.score2}", False, align='center', font=("Arial", 56, "normal"))

    def display_score(self):
        DrawScore(self.score1, -70, self.height / 2 - 15)
        DrawScore(self.score2, 50, self.height / 2 - 15)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align='center', font=("Arial", 12, "normal"))
