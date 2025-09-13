class Animal:
    def __init__(self,name,age,can_fly):
        self.name = name
        self.age = age
        self.can_fly = can_fly
    def speak(self):
        print("animal")
        
        
class dog(Animal):
    def __init__(self,name,age,can_fly):
        super().__init__(name,age,can_fly) 
    def speak(self):
        print("dog")
     
a = dog("joy",25,True)

print(a.name)
a.speak()        

Animal.speak(a)  #directly call parent speak()