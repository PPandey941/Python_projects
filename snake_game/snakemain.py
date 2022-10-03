# I have made a classic game of snake and food using python, it even saves the high score.
# use the arrow keys to play

import time
from turtle import Screen, Turtle
from snake import Snake
from snakefood import Food
from snakescoreboard import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
pos = 0
pss = Snake()
Fo = Food()
score = scoreboard()



screen.listen()
screen.onkey(key="Up", fun=pss.up)
screen.onkey(key="Down", fun=pss.down)
screen.onkey(key="Right", fun=pss.right)
screen.onkey(key="Left", fun=pss.left)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    pss.move()
    if pss.head.distance(Fo) < 15:
        Fo.refresh()
        pss.extend()
        score.increase_score()
    if pss.head.xcor() > 280 or pss.head.xcor() < -280 or pss.head.ycor() > 280 or pss.head.ycor() < -280:
        score.reset()
        pss.reset_snake()
    for segments in pss.segments[1:]:
        if pss.head.distance(segments) < 10:
            score.reset()
            pss.reset_snake()





screen.exitonclick()