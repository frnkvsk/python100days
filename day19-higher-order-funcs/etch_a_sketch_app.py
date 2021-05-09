from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_reverse():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key='f', fun=move_forward)
screen.onkey(key='r', fun=move_reverse)
screen.onkey(key='e', fun=turn_left)
screen.onkey(key='t', fun=turn_right)
screen.onkey(key='d', fun=clear)
screen.exitonclick()