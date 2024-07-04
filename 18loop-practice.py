'''enter height,print total number of student,total of height'''


height=input().split()

for i in range(0,len(height)):
 height[i]=int(height[i])

#total height
total_h=0
for a in range(0,len(height)):
 total_h+=height[a]

print(f"total height: {total_h}")   

#total student
total_s=0
for a in range(0,len(height)):
 total_s+=1

print(f"total student: {total_s}")  


'''we can also use this

total_h=0
for a in height:
 total_h+=a

print(f"total height: {total_h}")   
'''

