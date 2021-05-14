from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.colors = ['red', 'green', 'blue', 'purple', 'yellow', 'gold']
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.draw_car(x, y)

    def draw_car(self, x, y):
        color = random.choice(self.colors)
        self.color(color)
        self.penup()
        self.goto(x, y)

    def move_car(self):
        x = self.xcor() - 5
        self.goto(x, self.ycor())

    def hide_car(self):
        self.hideturtle()