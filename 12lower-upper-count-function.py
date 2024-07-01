'''lower case,upper case and count() function'''

a=input("your name:")
b=input("your favourite persion name:")

x=a.lower()
y=b.upper()
z=x+y
print(z)

c=a.upper()
d=b.upper()
m=c+d

'''in m how many 'A' and 'Y' located
example if m= Diyajoyalaala
no. of Y is 2
no. of A is 5  
then print 25
'''
Y=m.count('Y')
A=m.count('A')

t=str(Y)+str(A)

print("love number is "+ str(t))