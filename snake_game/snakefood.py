from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("blue")
      self.shapesize(stretch_len=1, stretch_wid=1)
      self.penup()
      self.refresh()

    def refresh(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)




