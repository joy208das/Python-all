"""class is a blueprint for creating objects

example:
object: Car
class: blueprint of this car"""


class Student:
    name = "Joy"
    
    
s1 =  Student()   #s1 is a object 
print(s1.name)    
    
s2 = Student()  #s2 is an another object
print(s2.name)    

#another example
class Car :
    color = "blue"
    brand = "mercedes"
    
    
car1 = Car()
print(car1.color)
print(car1.brand)   