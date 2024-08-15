from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
end = False
user_bet = screen.textinput(title="Make your bet" ,prompt="Which turtle will win the race?Enter a color: ")
colors = ["red","orange","black","blue","purple","green"]

y_positions = [-70,-40,-10,20,50,80]

all_turtle = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-225, y = y_positions[turtle_index])
    all_turtle.append(tim)

if user_bet:
    end = True

while end:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
           end = False
           winning_color = turtle.pencolor()
           if winning_color == user_bet:
               print(f"You've won! The {winning_color} turtle is the winner!")
           else:
               print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()