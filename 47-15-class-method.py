"""Class method"""

# class Person:
#     name = "anonymous"
    
#     def changeName(self, name):
#         self.name = name
        
        
# p1 = Person()
# p1.changeName("joy das")
# print(p1.name)
# print(Person.name)

"""uporer ai code a p1.changName print korle joy das print hobe 
kintu Person.name print korle anonymous print hobe
class attribute change hocche na , 
construction/object ar name change hocche
class attribute chng korte Class method use kora hoy
self.__class__.name 
or
@classmethod use kora"""

class Person:
    name = "anonymous"
    
    # def changeName(self, name):
    #     self.__class__.name = name
    
    @classmethod
    def changeName(self, name):
        self.name = name   
        
p1 = Person()
p1.changeName("joy das")
print(p1.name)
print(Person.name)