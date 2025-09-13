class A:
    def __init__(self):
        self.a = 10
        
        
alu = A()

print(alu.__dict__)        

'''Every Python object stores its
attributes in a dictionary (__dict__).'''

