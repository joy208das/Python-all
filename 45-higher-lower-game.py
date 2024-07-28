import random

data=[
 {
    'name':'JOY',
    'follower':300,
    'country':'Bangladesh',
    'Description':'Artist'
 },
 {
    'name':'MESSI',
    'follower':300000,
    'country':'Argentina',
    'Description':'GOAT'
},
{
    'name':'dodo',
    'follower':500000,
    'country':'Bangladesh',
    'Description':'motku',
},
{
    'name':'Diya',
    'follower':700000000,
    'country':'Bangladesh',
    'Description':'bubu',
},
{
    'name':'puchu',
    'follower':1,
    'country':'Bangladesh',
    'Description':'😊',
},
{
    'name':'🤷‍♂️',
    'follower':50000000,
    'country':'Bangladesh',
    'Description':'😜',
},
]
print() 
score=0
end=True
while end:
    a=random.choice(data)
    b=random.choice(data)
    if a==b:
        b=random.random(data)

    print(f"A= Name:{a['name']},Country:{a['country']},Description:{'Description'}")
    print("Vs.")
    print(f"B= Name:{b['name']},Country:{b['country']},Description:{b['Description']}")
    
    A=int(a['follower'])
    B=int(b['follower'])

    your_choice=input("your choice(A or B) : ").upper()
    print()
    
      
    if A>B:
  
        if your_choice=='A':
            score+=1
            print(f"your are right, score:{score}")
            print()
            end=True
        elif your_choice=='B':
            print("you are wrong")
            print(f"total score:{score}")
            end=False
        
    else:
       if your_choice=='B':
            score+=1
            print(f"your are right, score:{score}")
            print()
            end=True
       elif your_choice=='A':
            print("you are wrong")
            print(f"total score:{score}")
            end=False
