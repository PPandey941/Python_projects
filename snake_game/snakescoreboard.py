from turtle import Turtle, Screen


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snakedata.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f"Score: {self.score} High score = {self.high_score}", move=False, align="center", font=('Arial', 15, 'normal'))
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snakedata.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score = {self.high_score}", move=False, align="center", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
