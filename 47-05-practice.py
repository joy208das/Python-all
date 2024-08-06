"""create student class that takes name and marks of 
3 subjects as arguments in constructor.then creat a method to 
print the average"""


class Student:
    
    def __init__(self,name,mark) :
        self.name=name
        self.mark=mark
        
    def out(self):
        sum = 0
        for n in self.mark:
            sum += n
            
        print(f"hi {self.name} your average is :{sum/3}")


a1 = Student("joy das", [80, 89, 96])  
a1.out()


# a1.name= "iron man"
# a1.out()
  #we can change the name by this 