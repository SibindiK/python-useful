from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        _new_x = self.xcor() + self.x_move
        _new_y = self.ycor() + self.y_move
        self.goto(_new_x, _new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
