import random
from turtle import Turtle, Screen

WIDTH = 500
HEIGHT = 500
screen = Screen()
screen.setup(WIDTH, HEIGHT)
colors = ['red','blue','green','orange','purple','gold']
startY = -50
turtles = []
for c in colors:
    tt = Turtle('turtle')
    tt.color(c)
    tt.penup()
    tt.setposition(-WIDTH / 2 + 10, startY)
    startY += 25
    turtles.append(tt)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

maxX = 0
while maxX < 225:
    index = random.randint(0, len(turtles)-1)
    move = random.randint(5, 25)
    turtles[index].forward(move)
    maxX = max(maxX, turtles[index].xcor())

winner = [turtles[i].color() for i in range(len(turtles)) if turtles[i].xcor() == maxX][0][0]
if winner == user_bet:
    print('You win!!!')
else:
    print('You lose.')
print(f"Turtle color {winner} is the winner.")

screen.exitonclick()