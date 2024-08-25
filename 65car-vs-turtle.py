from turtle import Turtle,Screen
from turtle65 import Toto
import time
from car65 import Car
import random
from score65 import Score

screen = Screen()

screen.setup(height =600, width = 600)
screen.bgcolor("white")
screen.title("Car VS. Turtle")
screen.tracer(0)
 
tim = Toto()       
car_m= Car()
score = Score()
           
end = True

screen.listen()

screen.onkey(tim.go_up,"Up")
screen.onkey(tim.go_down,"Down")
while end:
    time.sleep(0.1) 
    screen.update()
    car_m.car_create()
    car_m.car_move()
    
    for n in car_m.car:
        if n.distance(tim)<20:
          end = False
          score.game_over()
          
          
          
    if tim.ycor() == 290 :
        tim.goto(0,-280)
        car_m.level()       
        score.level_up()     
    
    
screen.exitonclick()
    