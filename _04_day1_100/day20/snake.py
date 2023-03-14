from turtle import Turtle


class Snake:
    """definition of snake"""
    def __init__(self):
        self.snake = []
        start_coordinates = [(0, 0), (-20, 0), (-40, 0)]
        for coord in start_coordinates:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(coord)
            self.snake.append(segment)
