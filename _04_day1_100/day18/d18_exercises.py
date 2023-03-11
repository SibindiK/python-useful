import turtle as tr
import random

tim = tr.Turtle()
tim.shape('turtle')
tr.colormode(255)
tim.speed("fastest")


def random_color():
    """generate a random r, g, b color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk():
    """perform a random walk"""
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    for _ in range(200):
        tim.pencolor(random_color())
        tim.forward(20)
        tim.setheading(random.choice(directions))


def draw_shape(sides):
    """draw a shape with given number of sides"""
    angle = 360/sides
    color = (random_color())
    tim.pencolor(color)
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


def draw_spirograph(gap_size):
    for rotation in range(int(360/gap_size)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(gap_size)

def main():
    #random_walk()
    # for count in range(3, 11):
    #     draw_shape(count)
    draw_spirograph(5)
    screen = tr.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
