from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-(self.width / 2) + 20, (self.width / 2) - 20)
        random_y = random.randint(-(self.height / 2) + 20, (self.height / 2) - 20)
        self.goto(random_x, random_y)