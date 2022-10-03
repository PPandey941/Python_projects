# It is a game in which our player has to cross the traffic cause by cars and reach
# the finish line, it can move only with the upward arrow key. The speed of cars
# increase after each level


import time
from turtle import Screen
from crossingplayer import Player
from crossingcar_manager import CarManager
from crossingscoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()



screen.listen()
screen.onkey(player.move_turtle, "Up")

num = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for c in car.all_cars:
        if player.distance(c) < 20:
            score.game_over()
            car.sp = 5
            game_is_on = False

    if player.ycor() > 280:
        score.score_increase()
        player.reset()
        car.speed()





screen.exitonclick()