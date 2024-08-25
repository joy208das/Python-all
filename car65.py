from turtle import Turtle
import random

colors=["red", "orange", "yellow", "green", "blue", "purple"]
speed = 5
movement_increment = 10

class Car(Turtle):
    
    
    def __init__(self):
        self.car=[]
        self.car_speed = speed
             
    def car_create(self):
        choice = random.randint(1,7)
        if choice == 1:
            tim = Turtle("square")
            tim.color(random.choice(colors))   
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.penup()
            y_p = random.randint(-250,250)
            tim.goto(300,y_p)
            self.car.append(tim)
            
    def car_move(self):
        for n in self.car:
            n.backward(self.car_speed)
            
    def level(self):
        self.car_speed += movement_increment
        
                    
            
         
        