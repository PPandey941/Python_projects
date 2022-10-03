# It is a pong game when you look at the screen the right paddle is controlled by arrow key
# UP and DOWN and the left paddle is controlled by key "w" and "s". If one side misses the other
# gets the point.

from turtle import Screen
from pongpaddles import Pads
from pongball import Ball
from pongscore import Scoreboard
import time
sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong")
sc.tracer(0)
paddle = Pads(370)
paddle_2 = Pads(-370)
bal = Ball()
score = Scoreboard()
# The default size of the turtle is 20 x 20. So to get a size of 100 x 20 we stretch width by 5


sc.listen()
sc.onkey(paddle.move_f, "Up")
sc.onkey(paddle.move_b, "Down")
sc.onkey(paddle_2.move_f, "w")
sc.onkey(paddle_2.move_b, "s")

game_on = True
while game_on:
    time.sleep(bal.speed)
    sc.update()
    bal.move()
    if bal.ycor() > 280 or bal.ycor() < -280:
        bal.bounce()
    if bal.distance(paddle) < 30 and bal.xcor() > 340 or bal.distance(paddle_2) < 30 and bal.xcor() < -340:
        bal.paddle_strike()


    if bal.xcor() > 380:
        bal.reset_position()
        score.add_l_score()

    if bal.xcor() < -380:
        bal.reset_position()
        score.add_r_score()




sc.exitonclick()