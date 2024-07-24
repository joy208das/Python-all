import random

print("Welcome to the number guessing GAME!")
print("I am thinking of a number between 1 to 100")
actual_number = random.randint(1, 100)

dificulty = input("Choose a difficulty level (easy or hard): ").lower()

if dificulty == 'easy':
    attempts = 10
elif dificulty == 'hard':
    attempts = 5
else:
    print("Invalid difficulty level! Defaulting to easy.")
    attempts = 10

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))

    if guess_number > actual_number:
        print("Too high")
        print("Guess again")
    elif guess_number < actual_number:
        print("Too low")
        print("Guess again")
    else:
        print("You win")
        break

    attempts -= 1

if attempts == 0:
    print(f"You've run out of attempts! The number was {actual_number}")




'''
import random

print("Welcome to the number guessing GAME!")
print("I am thinking a number between 1 to 100")
actual_number=int(random.randint(1,100))

print(actual_number)

dificulty=input("choose a dificulty level(easy or hard): ")

attempts=[]
if dificulty=='easy':
    attempts=10
    for n in range(0,attempts):
      print(f"you have {attempts} attempts remaining to guess the number")
      guess_number=int(input("make a guess: "))
      if attempts>0:
        if  guess_number>actual_number:
            print("too high")
            print("guess again")
        elif guess_number<actual_number:
            print("too low")
            print("guess again")
        else :
            print("you win")  
      else :
        print("you finish")      
      attempts=attempts-1
 
elif dificulty=='hard':
    attempts=5
    for n in range(0,attempts):
      print(f"you have {attempts} attempts remaining to guess the number")
      guess_number=int(input("make a guess: "))
      if attempts>0:
        if  guess_number>actual_number:
            print("too high")
            print("guess again")
        elif guess_number<actual_number:
            print("too low")
            print("guess again")
        elif guess_number==actual_number:
            print("you win")   

      attempts=attempts-1

if attempts==0:
   print("you lose")
      

'''    
