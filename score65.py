from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("blue")
        self.penup()
        self.goto(-260,260)
        self.hideturtle()
        self.update()
        
        
    def update(self):
        self.write(f"Level: {self.level}", align ="center" , font =("arial",10,"normal")) 
            
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align ="center" , font =("arial",25,"normal"))    
          
    
    def level_up(self):
        self.level += 1
        self.clear()
        self.update()
        