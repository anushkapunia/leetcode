class Solution(object):
    def sortedSquares(self, nums):
        l = []
        for num in nums:
            l.append(num*num)
        
        n= len(l)
        l.sort()
        return l
        
            