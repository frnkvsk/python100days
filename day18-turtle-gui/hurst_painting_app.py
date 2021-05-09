import turtle as t
import random
import colorgram_app as cg

colors = cg.get_rgb_colors()
hurst = t.Turtle()
t.colormode(255)
hurst.speed('fastest')
hurst.shape('arrow')
startY = -200
startX = -200
hurst.penup()
hurst.hideturtle()
for i in range(10):
    startY += 50
    hurst.setposition(startX, startY)
    for j in range(10):
        c = random.choice(colors)
        hurst.dot(20, c)
        hurst.forward(50)

screen = t.Screen()
screen.exitonclick()