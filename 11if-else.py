'''conditional statement'''

print("wlcm to the rollercoaster!")
height= int(input("What is your height in cm?"))

if height> 120:
  print("you can ride the rollercoaster!")
else:
  print("Sorry,you can't")  


#even or odd
print("even/odd")

a=int(input('enter a number:'))

if a%2==0 :
 print("even")
else :
  print("odd")  

#elif 
#exam paper
  
print("Exam result")

x=int(input("enter mark:"))

if x>0 and x<=30:
 print('fail')
elif x>30 and x<80:
  print("A")
elif x>80 and x<=100:
  print("A+")
else:
  print("invalid number")     
