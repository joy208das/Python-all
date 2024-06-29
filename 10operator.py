'''
a**b - this means a^b

'''
print(2**3)

#exercise(BMI)

height=float(input("height:"))
weight=float(input("weight:"))

x=weight/(height**2)
print(x)
#for printing the bmi in integer number
a=str(int(x))
print("your BMI:" + a)

#round() function
print(round(8/3,2))  #8/3=2.666666.. for print 2 digit after point,we need to use round() function

print(round(2.666666,3))

#for print integer number like 2.66=2 use '//'
print(8//3) 
print(8/3) #this will return floating number

#f-String
'''instead of using str() function 
we can use f-String
f"{varialbe},..."
'''

score=0
height=1.8
isWinnig=True
print(f"your score is {score},your height is {height}, you ar winning is:{isWinnig}")