"""Create account class with 2 attributes -
balance and account no.
Create methods for debit,credit and printing the balance"""

class Account:
    def __init__(self, balance , account):
        self.balnc= balance
        self.acc= account
      
    #debit method    
    def debit(self, amount):
        self.balnc -= amount
        print(f"Rs. {amount} was debit ")
        print("total balance= ",self.get_balance())
    #credit method    
    def credit(self, amount):
        self.balnc += amount
        print(f"Rs. {amount} was credit ")   
        print("total balance= ",self.get_balance())
        
    def get_balance(self):
        return self.balnc   
    
         
a1 = Account(10000 , 2510)   
a1.debit(1000)     
a1.credit(500)

print(f"total balance: {a1.balnc}")
print(a1.acc)