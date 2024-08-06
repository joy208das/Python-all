"""Methods are function that belong to objects.
class ar bitor j funciton leka hoy tai methods.."""

class Student :
    def __init__(self, fullname, mark) :
         self.name = fullname
         self.mark = mark
         
         
    def welcome(self) :        #methods
        print("welcome student," , self.name)
        
    def get_marks(self):
        return self.mark
        
            
s1 = Student("joy",80)
s1.welcome()    
print(s1.get_marks())    
