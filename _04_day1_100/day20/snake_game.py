from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# screen.tracer(0)


def main():
    game_is_on = True
    player = Snake()

    while game_is_on:
        for segment in player.snake:

            segment.forward(20)


if __name__ == "__main__":
    main()
    screen.exitonclick()
