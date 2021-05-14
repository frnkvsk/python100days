from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.x = position[0]
        self.y = position[1]
        self.goto(position)

    def move(self, position):
        self.goto(position)