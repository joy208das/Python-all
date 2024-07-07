'''reeborg's world'''
#Alone- make squre in each block
def left_move():
    turn_left()
    turn_left()
    turn_left()
left_move()
turn_left()
turn_left()
move()
left_move()
move()
left_move()
move()
left_move()
move()


#Hurdle_1
def right_move():
    turn_left()
    turn_left()
    turn_left()
def first():
    turn_left()
    move()
    right_move()
    move()
    right_move()
    move()
    turn_left()
    
def do_it():
   move()
   first()

for step in range(6):    
 do_it()


#Hurdle-2
def right_move():
    turn_left()
    turn_left()
    turn_left()
def first():
    turn_left()
    move()
    right_move()
    move()
    right_move()
    move()
    turn_left()
    
def do_it():
   move()
   first()

while not  at_goal(): 
 do_it()


 #Hurdle-3
def right_move():
    turn_left()
    turn_left()
    turn_left()
def first():
    turn_left()
    move()
    right_move()
    move()
    right_move()
    move()
    turn_left()
    
def do_it():
   
   first()

while not  at_goal():
    if wall_in_front():
         do_it()
    else:
        move()



#Maze
        
def right_move():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        right_move()
        move()   
    elif front_is_clear():
        move()
    else:
       turn_left()
                   

#problem_world
       
def right_move():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        right_move()
        move()   
    elif front_is_clear():
        move()
    else:
       turn_left()
           
