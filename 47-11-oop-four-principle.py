"""3.Inheritance:
When one class(child/derived) derives the properties and methods of 
another class(parent/base).

main class ar bitor child class call kore amon ta bujay
"""

class Car():
    
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop() :
        print("car stoppe..")   
    
    
class Tata(Car):
    def __init__(self, name):
        self.name = name
        
        
car1 = Tata("tatan")       
car1.start()    


"""there are 3 types of Inheritance 
1.Single inheritance (single base class and derived class takbe,example:uporer code)
2.Multi-level inheritance
3.Multiple inheritance

"""

