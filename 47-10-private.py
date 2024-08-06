"""private :

password , account_no etc. agulo private thake 
class ar bitor kuno attribute k private korte 
attribute ar age double underscore dite hoy

self.__account_pass

class ar biare __account_pass print korte gele ta r hobe na
tobe class ar bitore kaj kora jay



"""

class Person:
    def __init__(self, account_no , account_pass):
      self.account_no = account_no
      self.__account_pass =  account_pass
      
    def __hello(self):
      print("hello person!")

    
a1 =  Person("1234","abcd") 
a1.__hello()
print(a1.__account_pass)  

"""Private attributes and methods are meant to be used only within the class 
and are not accessible from outside the class""" 

# class Personn:
#     __name = "anonymous"
    
#     def __helo(self):
#       print("hello person!")

#     def welcome(self):
#         self.__helo()
        
# p1 =  Personn() 
# p1.welcome()

'''run this code or dryrun'''
 
   