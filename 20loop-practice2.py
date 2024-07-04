#find longest height

height=input().split()
for i in range(0,len(height)):
 height[i]=int(height[i])

max=height[0]
for a in range(0,len(height)):
 if max<height[a]:
   max=height[a]
print(f"the longest h is:{max}")   


#find total of even number

target=input()
sum=0
for n in range(1,int(target)+1):  #sum of (1-target) 
 if n%2==0:
  sum=sum+n
print(f"total of even number: {sum}")  

