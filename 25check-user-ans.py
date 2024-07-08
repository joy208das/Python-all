'''how to check the user's answer'''

word_list=['jooy','makal','buuka']

import random
chosen_word = random.choice(word_list)
print(chosen_word)
guess=input("guess a letter: ")

for a in range(0,int(len(chosen_word))):
    if chosen_word[a]==guess:
       print("yes")
    else:
        print("no")  
