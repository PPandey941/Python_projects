# In this game you are asked for a making a guess as to which color of tortoise will win
# The one who makes the right guess wins

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Choose a colour.")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [30, 60, 90, 0, -30, -60]
all_turtles= []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230, y=y_pos[i])
    all_turtles.append(tim)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You have won. {win_color} turtle is the winner!!")
            else:
                print(f"You have lost. {win_color} turtle is the winner!!")

        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)




screen.exitonclick()