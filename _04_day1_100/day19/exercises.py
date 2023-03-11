from turtle import Screen, Turtle

screen = Screen()
t1 = Turtle()


def move_forward():
    t1.forward(10)


def move_backward():
    t1.backward(10)


def move_counter_clockwise():
    t1.left(10)


def move_clockwise():
    t1.right(10)


def clear_drawing():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()


def main():
    screen.listen()
    screen.onkey(fun=move_forward, key='w')
    screen.onkey(fun=move_backward, key='s')
    screen.onkey(fun=move_counter_clockwise, key='a')
    screen.onkey(fun=move_clockwise, key='d')
    screen.onkey(fun=clear_drawing, key='c')
    screen.exitonclick()


if __name__ == "__main__":
    main()
