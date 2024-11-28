class Solution(object):
    def missingNumber(self, nums):
        s = sum(nums)
        n = len(nums)
        s2 = (n*(n+1))//2
        
        return s2-s
        