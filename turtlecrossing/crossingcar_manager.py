from turtle import Turtle
import random
COLORS =["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.sp = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            r = random.randint(-250, 250)
            new_car.goto(280, r)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.sp)

    def speed(self):
        self.sp = self.sp + MOVE_INCREMENT








