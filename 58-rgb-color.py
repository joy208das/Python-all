import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
    
directions = [0, 90 , 180 , 270]
tim.pensize(15)
tim.speed("fastest")

for a in range(200):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))
 

# tim.speed(20)

# for n in range(50):
#     tim.circle(50)
#     tim.right(10)
