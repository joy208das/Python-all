

class dong:
    def __init__(self, *name):
        self.name = name
        
    def display(self):
        print(*self.name)        
a = dong("joy", "das")        
        
a.display()        