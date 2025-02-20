# # Taking space-separated input in one line
# arr = list(map(int, input("Enter elements: ").split()))
# print(arr)


n = int(input("enter size: "))

arr = []

for a in range(n):
    arr.append(int(input()))
    
    
for x in arr:
    print(x , end=" ")    