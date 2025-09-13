"""list = [1,2,3]

rotate it right to left
after 1st rotation 3,1,2
after 2nd rotation 2,3,1
after 3rd rotation 1,2,3

the size of the list is 3
the rotation will be 3 times"""


n = int(input())

a = list(map(int,input().split()))

for i in range(n):
    a.insert(0,a.pop())
    print(a)
  
  
"""
This line of Python code performs a right rotation of the list a by one position. Let's break it down:

a.pop():

The pop() method removes and returns the last element of the list a.
So, if a is [1, 2, 3], then a.pop() will:
Remove 3 from the list.
Return the value 3.
After this, a becomes [1, 2].
a.insert(0, ...):

The insert(index, value) method inserts value into the list a at the given index.
In this case, index is 0, which means it inserts the value at the beginning of the list.
The value being inserted is the result of a.pop(), which is the last element that was removed.
Putting it together:

a.pop() takes the last element of the list.
a.insert(0, ...) inserts that element at the beginning of the list.
Therefore, the last element is moved to the first position, effectively rotating the list to the right by one position.

Example:

If a is [1, 2, 3]:
a.pop() returns 3, and a becomes [1, 2].
a.insert(0, 3) inserts 3 at the beginning, so a becomes [3, 1, 2]."""  
  