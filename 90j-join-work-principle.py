'''reverse the vowels
example: 
input; leetcode
output: leotcede'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        au =[]
        vowels = "aeiouAEIOU"
        
        result = ''.join([char for char in s if char in vowels])
        
        new = result[::-1]
        
        re= ''.join('_' if char in vowels else char for char in s) 
        
        rep_in = 0
        for i in re:
            if i=='_':
             au.append(new[rep_in])
             rep_in+=1
            else :
                au.append(i)     
          
        return  ''.join(au)
        
        
s = input()
out = Solution()
output =  out.reverseVowels(s)
print(output)