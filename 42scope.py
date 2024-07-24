'''scope'''


#Local scope

def drink_potion():
    potion_strenght=2         #local variable
    print(potion_strenght)   

drink_potion()


#Global scope

player_health=10      #Global scope

def drink_potion():
    potion_strenght=2         #local variable
    print(player_health)   

drink_potion()
print(player_health)

"""Modifying global scope"""

enemies=1

def modify():
    global enimies
    enemies + 1
    print(f"1st is: {enemies}")

modify()
print(f"2nd is: {enemies}")    


'''without using global '''
friend=2

def m():
    print(f"1st friend: {friend}")
    return friend + 1
    
frind=m()
print(f"2nd friend: {friend}")  
 

#Global constant

PI=3.1416
URL="https://chatgpt.com/c/2d9a2c79-57a5-4713-9879-b1bd5260693d"

#these upper case varibale are global constant

