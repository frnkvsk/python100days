from turtle import Turtle


class Score(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.penup()
        self.width = width
        self.height = height
        self.score = 0
        self.high_score = 0
        self.goto(-10, self.height / 2 - 30)
        self.color('white')
        self.hideturtle()
        self.read_high_score()
        self.update_scoreboard()

    def read_high_score(self):
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.read())

    def set_high_score(self):
        with open('high_score.txt', 'w') as file:
            file.write(str(self.score))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score}  High Score: {self.high_score}", False, align='center', font=("Arial", 12, "normal"))

