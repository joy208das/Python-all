'''for loop'''

fruits=["apple","banana","orange"]

for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
    print(fruits)
print(fruits)


#another
name="joy"
for i in name:
 print(i)


#range function

for k in range(5):    #print 0-4  
 print(k)  

for i in range(1,10):     #print 1-9
 print(i)
 
for i in range(1,10,3):  #everytime add 3
 print(i)

s_h=input().split()
for n in range(0,len(s_h)):
    s_h[n]=int(s_h[n])
    print(s_h[n])

 
 
 