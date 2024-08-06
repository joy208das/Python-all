'''super method'''

class Car():
    def  __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("started...")
    @staticmethod
    def stop():
        print("stopped...")        
        
class Tata(Car):
    def __init__(self , name, type):
        
        super().__init__(type)
        self.name = name  
        super().stop()      
        
car1 = Tata("tatan","gigo")
car1.start()        