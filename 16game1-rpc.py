import random

''''game'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("ROCK PAPER SCISSORS")
game_images=[rock,paper,scissors]
my_choice=int(input("if you want rock print 0\nif you want paper print 1\nif you want scissors print 2\n"))
print(f"My choice:{game_images[my_choice]}")

computer_choice=random.randint(0,2)
print(f"computer:{game_images[computer_choice]}")


if my_choice ==0 and computer_choice==1:
 print("YOU DEAD\n")
elif my_choice ==1 and computer_choice==2:
 print("YOU DEAD\n")
elif my_choice ==2 and computer_choice==0:
 print("YOU DEAD\n")
elif my_choice == computer_choice:
 print("DRAW\n")
elif my_choice >2:
 print("YOU DEAD\n")
else:
 print("BUBU WIN\n")
