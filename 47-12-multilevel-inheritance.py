"""Multi-level Inheritance"""
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
        
        
class Type(Tata):
    def __init__(self , type):
        self.type = type
        
        
a1 =  Type("ju")

a1.start()                