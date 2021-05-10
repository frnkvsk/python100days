from turtle import Screen
from snake_body import Snake
import time

WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake(WIDTH, HEIGHT)

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
