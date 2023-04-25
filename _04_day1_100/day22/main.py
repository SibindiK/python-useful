from turtle import Screen
from turtle import Turtle
import time

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


def create_screen():
    _screen = Screen()
    _screen.bgcolor("black")
    _screen.setup(width=800, height=700)
    _screen.title("Pong")
    _screen.tracer(0)
    return _screen


def main():
    game_is_on = True
    ball_in_play = True

    screen = create_screen()
    r_pad = Paddle(350, 0)
    l_pad = Paddle(-350, 0)
    ball = Ball()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(r_pad.go_up, "Up")
    screen.onkey(r_pad.go_down, "Down")
    screen.onkey(l_pad.go_up, "w")
    screen.onkey(l_pad.go_down, "s")

    while game_is_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # detect collision with the top or bottom wall
        if ball.ycor() > 330 or ball.ycor() < -330:
            ball.bounce_y()

        # detect collision with the paddles
        if ball.distance(r_pad) < 50 and ball.xcor() > 320 or \
                ball.distance(l_pad) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # detect if ball has been missed by right pad
        if ball.xcor() > 380:
            ball.reset_ball()
            scoreboard.inc_l_score()
        # detect if ball has been missed by left pad
        if ball.xcor() < -380:
            ball.reset_ball()
            scoreboard.inc_r_score()

    screen.exitonclick()


if __name__ == "__main__":
    main()
