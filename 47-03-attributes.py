"""Class & Instance Attributes"""
"""suppose all the students are studying in the same school,
so we don't need to parameterized again again 
like self.school_name="abc"
we can creat a variable before create a init function.

if we creat another variable named:
name = "abcd..."
name is also an attribute in self parameter
self.name = fullname
then which will be work
abcd... or Joy D@s
here name="abcd..." is a class attribute
and self.name is a object attribute
obj attr > class attr
so Joy D@s will be print 
"""

class Student:
    #parameterized constructors
    school_name = "Abc school"
    name = "abcd..."
    def __init__(self, fullname, marks):      
        self.name = fullname    
        self.mark = marks       
        print("adding new student in Database...")
    
    
    
s1 =  Student("Joy D@s", 80)  
print(s1.name)  
print(s1.mark)
print(s1.school_name)
# s2 = Student("pupu")
# print(s2.name)
# print(s2.school_name)