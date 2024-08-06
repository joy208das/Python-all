"""Property decorator"""

# class Student():
#     def __init__(self, bang,eng,math):
#         self.bang = bang
#         self.eng =  eng
#         self.math =  math
#         self.percentage = (self.bang+self.eng+self.math)/3
        
        
# a1 = Student(80,96,81)
# print(f"{a1.percentage}%")

# a1.math = 90
# print(f"{a1.percentage}%")

"""in this code when I change the mark of math 
the percentage remain same 
so we need property decorator here"""


class Student():
    def __init__(self, bang,eng,math):
        self.bang = bang
        self.eng =  eng
        self.math =  math
    @property
    def percentage(self):    
     return (self.bang+self.eng+self.math)/3
        
        
a1 = Student(80,96,81)
print(f"{a1.percentage}%")

a1.math = 63
print(f"{a1.percentage}%")


        
        