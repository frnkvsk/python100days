from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display_score()
        # self.grids()

    def display_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-285, 250)
        self.write(f"Level:  {self.score}", False, 'left', ('Times New Roman', 18, 'bold'))

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        t = Turtle()
        t.hideturtle()
        t.write('GAME OVER', False, 'center', ('Times New Roman', 18, 'bold'))

    def grids(self):
        # Only used for debugging
        for i in range(-300, 300, 10):
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(-280, i)
            t.write(i, False, 'left', ('Arial', 8, 'normal'))