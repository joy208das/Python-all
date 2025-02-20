'''
we can't store the sorted array of heights in
exp variable using sort()

for this we need to use sorted() function

'''

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp = sorted(heights)
        a=0
        for i in range(len(heights)):
            if exp[i]!=heights[i]:
                a+=1
                
        return a        
        
        
        
        
        
        
heights = list(map(int,input('enter h: ').split()))

ou =Solution()
out = ou.heightChecker(heights)        
print(out) 