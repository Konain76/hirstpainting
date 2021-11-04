# import colorgram
#
# colors = []
# a = colorgram.extract("image.jpg", 20)
# for i in a:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     colors.append((r, g, b))
# print(colors)
import turtle
from turtle import Turtle, Screen
import random
colors = ["red", "black"]
tim = Turtle()
turtle.colormode(255)
size = 10
tim.speed("fastest")

def dots(s):
    for _ in range(9):


        tim.pendown()
        tim.dot(25, random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(25, random.choice(colors))
        tim.penup()
    tim.goto(0, s)


for i in range(50, 401, 50):
    print(i)
    dots(i)




screen = Screen()
screen.exitonclick()
screen.screensize(2000, 1500)
