from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.display_score()

    def increment(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", align=ALIGNMENT, font=FONT)
