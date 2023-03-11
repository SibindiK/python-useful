from turtle import Screen, Turtle
import random

screen = Screen()
colours = ["red", "yellow", "blue", "orange", "purple", "green", "brown", "violet"]


def user_choice():
    pass


def create_turtles():
    turtles = []
    x_pos = -300
    y_pos = 200
    for colour in colours:
        name = colour + "_turtle"
        name = Turtle(shape="turtle")
        name.color(colour)
        name.penup()
        name.goto(x_pos, y_pos)
        y_pos -= 50
        turtles.append(name)
    return turtles


def move_forward(my_turtle):
    my_turtle.pendown()
    my_turtle.forward(random.randint(10, 20))
    return my_turtle.xcor(), my_turtle.color()


def main():
    x_win_pos = 300
    winner_status = ()
    is_winner = False

    my_turtles = create_turtles()
    user_bet = screen.textinput("Make a bet", "Which colour turtle will win? e.g. blue")
    while not is_winner:
        winner_status = move_forward(random.choice(my_turtles))
        if winner_status[0] >= x_win_pos:
            is_winner = True

    print(winner_status[1][0])

    screen.exitonclick()


if __name__ == "__main__":
    main()
