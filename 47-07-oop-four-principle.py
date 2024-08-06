"""opp
1.Abstraction: 
hiding the implementation details of a class and only showing
the essential features to the users.
example: akti car ar bitore engine kivabe kaj kore ta driver deke na,
ja dekar proyojon nei

2.Encapsulation:
Wrapping data and functions into 
a single unit(object)
ja age kore asechi ta sob encapsulation
data+function....diye sob kichu

3.Inheritance:
When one class(child/derived) derives the properties and methods of 
another class(parent/base).

4.Polymorphism: Operator Overloading
when the same operator is allowed to have different meaning according 
to the context.

"""


'''Abstraction'''

class Car:
    def __init__(self):
         self.acc = False
         self.brk = False
         self.clutch = False
         
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")
             
car1 = Car()
car1.start()         

#akane def __init__(self) &   start(self) ar kaj gulo hide thake
#this is abstraction