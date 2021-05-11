from turtle import Screen
from snake_body import Snake
import time
from food import Food
from score_board import Score

score = 0
WIDTH = 600
HEIGHT = 600
LEFT_WALL_X = -WIDTH / 2 - 20
RIGHT_WALL_X = WIDTH / 2 + 20
TOP_WALL_Y = HEIGHT / 2 + 20
BOTTOM_WALL_Y = -HEIGHT / 2 - 20
screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake(WIDTH, HEIGHT)
food = Food(WIDTH, HEIGHT)
score = Score(WIDTH, HEIGHT)

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() <= LEFT_WALL_X or snake.head.xcor() >= RIGHT_WALL_X or snake.head.ycor() >= TOP_WALL_Y or snake.head.ycor() <= BOTTOM_WALL_Y:
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
