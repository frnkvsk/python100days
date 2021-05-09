from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_reverse():
    t.backward(10)

screen.listen()
screen.onkey(key='f', fun=move_forward)
screen.onkey(key='r', fun=move_reverse)
screen.exitonclick()