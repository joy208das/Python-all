class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        alu = int("".join(map(str,num)))
        bulu = alu + k
        a= list(map(int,str(bulu)))
        return a
    
num= list(map(int,input('enter list: ').split()))   
k=int(input('enter key: ')) 
ou = Solution()
out= ou.addToArrayForm(num,k)
print(out)