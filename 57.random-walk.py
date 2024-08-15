from turtle import Turtle
import random

tim = Turtle()
colors = ["red", "green" ,"blue", "brown", "wheat", "black" ,"pink"]
directions = [0, 90 , 180 , 270]
tim.pensize(15)
tim.speed(5)

for a in range(200):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))