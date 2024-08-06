"""Constructor

all classes have a function called __init__() , 
which is always excuted when the object is being initiated

akti class a  jodi ditiyo arekti object toiri kori,
tahole class autometically init function k call kore dibe
like ager code a s2
"""

class Student :
    #default constructor
    def __init__(self) :
        pass

class Student:
    #parameterized constructors
    def __init__(self, fullname):      #self is a 1st parameter which is directly indecate the s1 object; fullname is a parameter of s1's value("Joy D@s")
        self.name = fullname           #name is a new variable 
        print("adding new student in Database...")
    
    
    
s1 =  Student("Joy D@s")  
print(s1.name)  
s2 = Student("pupu")
print(s2.name)
    
"""here name(s1.name) is a attributes
"""
