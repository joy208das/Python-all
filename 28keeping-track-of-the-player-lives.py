'''keeping-track-of-the-player's-lives'''
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['jooy','makal','buuka']

chosen_word = random.choice(word_list)
print(chosen_word)
 

display=[]
for a in range(0,int(len(chosen_word))):
   display+='_'
print(display)    


end=True
x=len(stages)-1

while end:
    guess=input("enter word: ")
    
    count=0  
    for a in range(0,int(len(chosen_word))):
     if chosen_word[a]==guess:
        display[a]=guess  
        count+=1

    if count==0:
        print(stages[x])
        x-=1
    if x<=0:
     print("you dead")
     end=False
    print(display)
     

    if '_' not in display:
       end =False
       print("live")