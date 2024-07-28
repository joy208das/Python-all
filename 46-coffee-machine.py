"""coffee machine"""

water=100
milk=1000
coffee=500
money=0

end=True

data=[

    {
      'water':50,
      'coffee':5,
      'milk':25,
      'money':90
    },
     {
      'water':40,
      'coffee':7,
      'milk':30,
      'money':150
    },
     {
      'water':40,
      'coffee':10,
      'milk':40,
      'money':200
    }

]


while end:
    
    a=input("What would you like? (espresso/latte/cappuccino): ")
    if a=='report':
     print(f"Water:{water}ml ,Milk:{milk}ml ,Coffee:{coffee}ml ,Money:{money}Tk ")
     continue
     

    print("Please insert money: ")
    
    c=int(input("How many 10 TK notes?: "))
    d=int(input("How many 20 TK notes?: "))
    e=int(input("How many 50 TK notes?: "))
    f=int(input("How many 100 TK notes?: "))
    g=int((c*10)+(d*20)+(e*50)+(f*100))
    
    if a=='espresso':
       A=data[0]
       
       if water>=A['water'] and milk>=A['milk'] and coffee>=A['coffee']:
        water=water-A['water']
        milk=milk-A['milk']
        coffee=coffee-A['coffee']
        if g>=A["money"]:
            print(f"Here is your change:{g-A['money']}")
            print("Enjoy your espresso coffee")
        else :
            print("Sorry that's not enough money,money refunded")   
       else:
          print("Sorry, there are not enough resources to make an espresso.")
       money=money+A['money'] 

    elif a=='latte':
       B=data[1]
       
       if water>=B['water'] and milk>=B['milk'] and coffee>=B['coffee']:
        water=water-B['water']
        milk=milk-B['milk']
        coffee=coffee-B['coffee']
        if g>=B["money"]:
            print(f"Here is your change:{g-B['money']}")
            print("Enjoy your latte coffee")
        else :
            print("Sorry that's not enough money,money refunded")   
       else:
          print("Sorry, there are not enough resources to make a latte.")
       money=money+B['money']  

    elif a=='cappuccino':
       C=data[2]
       

       if water>=C['water'] and milk>=C['milk'] and coffee>=C['coffee']:
        water=water-C['water']
        milk=milk-C['milk']
        coffee=coffee-C['coffee']
        if g>=C["money"]:
            print(f"Here is your change:{g-C['money']}")
            print("Enjoy your cappuccino coffee")
        else :
            print("Sorry that's not enough money,money refunded")   
       else:
          print("Sorry, there are not enough resources to make a cappuccino.")
       money=money+C['money']  
  
      
     
     



