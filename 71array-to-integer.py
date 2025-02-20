"""input an array and make it into integer or string value"""
arr=[]

n= int(input("enter size"))

for n in range(n):
    a = input()
    arr.append(a)

num = int(''.join(map(str,arr)))
num2= int(str(num)[::-1]) #print in reverse position
print(num)
print(num2)


"""
map(str,arr) converts each elements in the array into a string 
''.join() ->
When you use ''.join(...) in Python, 
it joins or concatenates a list of strings into a single string.
The part before .join() (in this case, '') specifies the separator 
that will be placed between the strings being concatenated.

For example:

If you use '-'.join(['1', '3', '4']), it will return '1-3-4',
inserting a hyphen - between the elements.

If you use ','.join(['1', '3', '4']), 
it will return '1,3,4', inserting a comma , between the elements.


In your case, using ''.join(['1', '3', '4'])
(with an empty string '' as the separator) means the elements are 
joined together without any character in between, so it returns '134'.
"""