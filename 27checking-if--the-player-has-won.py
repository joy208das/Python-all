'''27checking-if--the-player-has-won'''


word_list=['jooy','makal','buuka']

import random
chosen_word = random.choice(word_list)
print(chosen_word)
 

display=[]
for a in range(0,int(len(chosen_word))):
   display+='_'
print(display)    

end=True

while end:
    guess=input("enter word: ")
        
    for a in range(0,int(len(chosen_word))):
     if chosen_word[a]==guess:
        display[a]=guess  
    print(display)

    if '_' not in display:
       end =False
       print("win")