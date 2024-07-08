'''replacing-blanks-with-guesses'''

word_list=['jooy','makal','buuka']

import random
chosen_word = random.choice(word_list)
print(chosen_word)
 

display=[]
for a in range(0,int(len(chosen_word))):
   display+='_'
print(display)    

guess=input("enter word: ")
       
for a in range(0,int(len(chosen_word))):
   
   if chosen_word[a]==guess:
     display[a]=guess       
print(display)