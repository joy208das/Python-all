# i=10

# for a in range(i,-1,-1):
#     print(i)
#     i=i-1
    
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        s = s.strip()  # Removes any trailing/leading spaces
        t = list(s)     # Convert the string into a list of characters
        
        for i in range(len(t) - 1, -1, -1):  # Start from the end of the string
            if t[i] == " ":
                break
            x += 1

        return x

# Input from the user
s = input('Enter your line: ')
a = Solution()
b = a.lengthOfLastWord(s)

print(b)



'''In this code:

len(t)-1 is the starting value.
-1 is the stopping value (since the range function excludes the 
stopping value, the loop will stop at 0).
-1 is the step, meaning the value of i will decrease by 1 in each iteration.
This will print the numbers from 9 to 0 in a decrementing order.'''
    