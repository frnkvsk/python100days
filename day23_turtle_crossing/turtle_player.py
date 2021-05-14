from turtle import Turtle


class Turtleplayer(Turtle):
    def __init__(self, height):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -height / 2 + 30)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)