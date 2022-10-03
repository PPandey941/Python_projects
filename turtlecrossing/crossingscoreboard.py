from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", align="center", font=("Courier", 24, "normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update()