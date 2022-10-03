from turtle import Turtle


class Pads(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(x, 0)

    def move_f(self):
        y_cord = self.ycor() + 20
        self.goto(self.xcor(), y_cord)

    def move_b(self):
        y_cord = self.ycor() - 20
        self.goto(self.xcor(), y_cord)

