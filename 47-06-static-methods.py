"""Static methods
methods that don't use the self 
parameter (work at class level)"""


class Student:
    
    def __init__(self,fullname):
        self.name = fullname
    
    @staticmethod    #(decorator) ata likle error asbe na 
    def college():    #self parameter nei
        print("metropolitan")
        
        
a1 = Student("joy")        
a1.college()