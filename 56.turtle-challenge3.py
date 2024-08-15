from turtle import Turtle
import random

tim = Turtle()
colors = ["red", "green" ,"blue", "brown", "wheat", "black" ,"pink"]
def draw_shape(num_sides):
    for a in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for a in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(a)