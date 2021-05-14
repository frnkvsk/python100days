from turtle import Turtle


class DrawScore:

    def __init__(self, num, x, y):
        self.segments = [[] for _ in range(5)]
        self.create_segments(x, y)
        self.draw_number(num)

    def create_segments(self, x, y):
        for i in range(0, 5):
            for j in range(0, 3):
                t = Turtle('square')
                t.shapesize(stretch_wid=.5, stretch_len=.5)
                t.goto(x + (j * 10), y - (i * 10))
                self.segments[i].append(t)

    def draw_number(self, num):
        if num == 0:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('black')
            self.segments[2][2].color('white')

            self.segments[3][0].color('white')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 1:
            self.segments[0][0].color('black')
            self.segments[0][1].color('black')
            self.segments[0][2].color('white')

            self.segments[1][0].color('black')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('black')
            self.segments[2][1].color('black')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('black')
            self.segments[4][1].color('black')
            self.segments[4][2].color('white')
        elif num == 2:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('black')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('white')
            self.segments[3][1].color('black')
            self.segments[3][2].color('black')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 3:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('black')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 4:
            self.segments[0][0].color('white')
            self.segments[0][1].color('black')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('black')
            self.segments[4][1].color('black')
            self.segments[4][2].color('white')
        elif num == 5:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('black')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 6:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('black')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('white')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 7:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('black')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('black')
            self.segments[2][1].color('black')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('black')
            self.segments[4][1].color('black')
            self.segments[4][2].color('white')
        elif num == 8:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('white')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
        elif num == 9:
            self.segments[0][0].color('white')
            self.segments[0][1].color('white')
            self.segments[0][2].color('white')

            self.segments[1][0].color('white')
            self.segments[1][1].color('black')
            self.segments[1][2].color('white')

            self.segments[2][0].color('white')
            self.segments[2][1].color('white')
            self.segments[2][2].color('white')

            self.segments[3][0].color('black')
            self.segments[3][1].color('black')
            self.segments[3][2].color('white')

            self.segments[4][0].color('white')
            self.segments[4][1].color('white')
            self.segments[4][2].color('white')
