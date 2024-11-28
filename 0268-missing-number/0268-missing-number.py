class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        x2 = 0
        x1 = 0
        for i in range(n):
            x2 = x2 ^ nums[i]
            x1 = x1^ (i+1)
        
        
        return x1^x2
        
        