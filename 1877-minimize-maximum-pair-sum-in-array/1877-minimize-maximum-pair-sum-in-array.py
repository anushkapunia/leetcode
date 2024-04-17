class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        sum = []
        for i in range(len(nums)):
            s= nums[i]+nums[len(nums)-i-1]
            sum.append(s)
        return max(sum)    
            
        
        
        
        