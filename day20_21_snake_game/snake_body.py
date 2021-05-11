from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
# STARTING_POSITIONS = [(60, 0), (40, 0), (20, 0), (0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.segments = []
        self.create_snake()
        self.direction = 0
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle('square')
        segment.speed('fastest')
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            x = self.segments[seg_num -1].xcor()
            y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.setheading(self.direction)
        self.head.forward(20)

    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def grow(self):
        self.add_segment(self.segments[-1].position())
