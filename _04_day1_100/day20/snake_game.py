import time
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def main():
    game_is_on = True
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    # detect key strokes to control movement of snake
    screen.listen()
    screen.onkey(snake.up, "Up")  # bind snake.up function to UP keyboard key
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            scoreboard.increment()

        # detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.display_game_over()
            game_is_on = False

        # detect collision with body
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.display_game_over()
                game_is_on = False


if __name__ == "__main__":
    main()
    screen.exitonclick()
