# I read somewhere that a Damien Hirst a painter made $200,000 just by making a painting
# that has dots arranged in a serial pattern, so I recreated it.
# I took the real image and imported colorgram to get the colours.


import turtle as tim
import random
import colorgram

#all the turtle functions like calling and setting screen
tim.colormode(255)
tim.showturtle()
tim.shape("turtle")
Screen = tim.Screen()

# making a list of random colors in rgb format

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

#running the turtle to draw the painting
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









Screen.exitonclick()