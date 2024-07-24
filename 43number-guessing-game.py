'''number guessing GAME'''
import random

print("Welcome to the number guessing GAME!")
print("I am thinking a number between 1 to 100")
actual_number=int(random.randint(1,100))


dificulty=input("choose a dificulty level(easy or hard): ")
def call(attempts):
   for n in range(0,attempts):
      print(f"you have {attempts} attempts remaining to guess the number")
      guess_number=int(input("make a guess: "))
      if attempts>0:
        if  guess_number>actual_number:
            print("too high")
        
        elif guess_number<actual_number:
            print("too low")
            
        elif guess_number==actual_number:
            print("you win") 
            break  
      if attempts>1:
        print("guess again")
      attempts=attempts-1

   if attempts==0:
      print(f"You've run out of attempts! The number was {actual_number}")

attempts=[]
if dificulty=='easy':
    attempts=10
    call(attempts)
elif dificulty=='hard':
    attempts=5
    call(attempts)    
 

      


