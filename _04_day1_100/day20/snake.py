from turtle import Turtle

START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING_RIGHT = 0
HEADING_UP = 90
HEADING_LEFT = 180
HEADING_DOWN = 270


class Snake:
    """definition of snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coord in START_COORDINATES:
            self.add_segment(coord)

    def add_segment(self, coord):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(coord)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def down(self):
        if not self.head.heading() == HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def left(self):
        if not self.head.heading() == HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)

    def right(self):
        if not self.head.heading() == HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)
