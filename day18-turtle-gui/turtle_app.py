
import turtle as t
import random
import colorgram_app as cg

tim = t.Turtle()
tim.shape('triangle')
# tim.color('green')
t.colormode(255)


""" draw square """
# for _ in range(4):
#     tim.forward(225)
#     tim.left(90)
# ----------------------------------------------

""" draw dashed line """
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# -----------------------------------------------

# colors = ["DarkGreen","DarkRed","DarkViolet","DarkTurquoise","DarkOrange","DeepPink","FireBrick","GoldenRod","Blue",
#           "BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue",
#           "Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan"]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

""" draw shapes """
# for i in range(3, 20):
#     color = random.choice(colors)
#     for _ in range(i):
#         tim.color(color)
#         tim.forward(50)
#         tim.right(360 / i)
# --------------------------------------------

""" random walk """
# directions = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# --------------------------------------------

""" draw Spirograph """
colorgrams = cg.get_rgb_colors()
tim.speed('fastest')
for _ in range(60):
    tim.color(random.choice(colorgrams))
    tim.circle(100)
    tim.right(6)


screen = t.Screen()
screen.exitonclick()