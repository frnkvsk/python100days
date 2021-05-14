from turtle import Turtle


def draw_center_line(height):
    line = Turtle('square')
    line.hideturtle()
    line.speed('fastest')
    line.penup()
    line.goto(0, height / 2)
    line.setheading(270)
    line.color('white')
    line.pensize(3)
    curr_height = height
    while curr_height > -height / 2:
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)
        curr_height -= 20
    line.showturtle()

class DrawCenterLine:

    def __init__(self, height):
        draw_center_line(600)

