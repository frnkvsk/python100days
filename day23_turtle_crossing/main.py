from turtle import Screen
from scoreboard import Scoreboard
from turtle_player import Turtleplayer
from car import Car
import time
import main
import random

WIDTH = 600
HEIGHT = 600
level = 0
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)
screen.listen()
turtleplayer = Turtleplayer(HEIGHT)
scorebrd = Scoreboard()
cars = []

game_on = True


def win():
    print('win')
    main.turtleplayer.hideturtle()
    main.level += 1
    main.scorebrd.update_score()
    main.turtleplayer = Turtleplayer(HEIGHT)


def move_up():
    main.turtleplayer.move_up()
    if main.turtleplayer.ycor() >= HEIGHT / 2 - 20:
        win()


screen.onkeypress(move_up, 'Up')
screen.onkeypress(turtleplayer.move_down, 'Down')


while game_on:
    capacity_cars = 60 + level * 10
    min_distance = max(25, 70 - level * 5)
    for c in cars:
        if c.distance(turtleplayer) < 20:
            scorebrd.game_over()
            game_on = False
    if game_on and len(cars) < capacity_cars:
        x = WIDTH / 2
        y = random.randint(int(-HEIGHT / 2 + 50), int(HEIGHT / 2 - 65))
        open_slot = True
        for c in cars:
            if c.distance((x, y)) < min_distance:
                open_slot = False

        if open_slot:
            car = Car(x, y)
            cars.append(car)
    if game_on:
        for c in cars:
            if c.xcor() < -WIDTH / 2:
                c.hideturtle()
                cars.remove(c)
            else:
                c.move_car()
        screen.update()
        time.sleep(0.1)


def game_over():
    main.game_on = False


screen.onkey(game_over, 'x')

screen.exitonclick()
