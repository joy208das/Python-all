"""Multiple Inheritance"""

class A():
    varA = "welcome to class A"

    
class B():
    varB = "wlcome to class B"
   
class C(A,B):
    varC ="WElcome to class C"    
    
        
        

a1 = C()
print(a1.varA)
print(a1.varB)       
          
