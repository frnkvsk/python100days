from turtle import Screen
from score_board import Score
from draw_center_line import DrawCenterLine
from paddle import Paddle
import main
from ball import Ball
import time

WIDTH = 900
HEIGHT = 600
active_player = 'left'
player_1_score = 0
player_2_score = 0
ball_position = (0, 0)
screen = Screen()
screen.tracer(0)
screen.listen()

turn = 'left'

screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game')
score = Score(WIDTH, HEIGHT, player_1_score, player_2_score)
paddle_1 = Paddle(-WIDTH / 2 + 30, -10)
paddle_2 = Paddle(WIDTH / 2 - 30, -10)


def move_up():
    if main.active_player == 'right':
        paddle_1.move_up()
    else:
        paddle_2.move_up()


def move_down():
    if main.active_player == 'right':
        paddle_1.move_down()
    else:
        paddle_2.move_down()


screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')


dcl = DrawCenterLine(600)

game_on = True


def game_over():
    main.game_on = False


screen.onkey(game_over, 'x')


while game_on:
    start_right = (10, 5)
    start_left = (-10, -5)
    ball = Ball((0, 0))
    if active_player == 'right':
        current_direction = start_left
    else:
        current_direction = start_right
    x = current_direction[0]
    y = current_direction[1]
    ball.hideturtle()
    curr_round = True
    while curr_round:
        time.sleep(.1)
        (X, Y) = (ball.xcor(), ball.ycor())
        (p1_x, p1_y) = (paddle_1.xcor(), paddle_1.ycor())
        (p2_x, p2_y) = (paddle_2.xcor(), paddle_2.ycor())
        if X >= WIDTH / 2 - 10:
            player_1_score += 1
            score = Score(WIDTH, HEIGHT, player_1_score, player_2_score)
            active_player = 'right'
            curr_round = False
            print(x, y, X, Y)
        elif X <= -WIDTH / 2 - 10:
            player_2_score += 1
            score = Score(WIDTH, HEIGHT, player_1_score, player_2_score)
            active_player = 'left'
            curr_round = False
            print(x, y, X, Y)
        elif Y >= HEIGHT / 2 - 10 or Y <= -HEIGHT / 2 + 10:
            y *= -1
        elif ball.xcor() >= WIDTH / 2 - 50 and ball.distance(paddle_2) < 50:
            print('hit right', ball.distance(paddle_2))
            x *= -1
            active_player = 'right'
        elif ball.xcor() <= -WIDTH / 2 + 50 and ball.distance(paddle_1) < 50:
            print('hit left', ball.distance(paddle_1))
            x *= -1
            active_player = 'left'
        ball.hideturtle()
        ball = Ball((X + x, Y + y))
        screen.update()
    ball.hideturtle()

screen.exitonclick()
