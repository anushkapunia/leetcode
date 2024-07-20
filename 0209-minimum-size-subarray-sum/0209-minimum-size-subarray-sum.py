class Solution(object):
    def minSubArrayLen(self, target, nums):
        l , r = 0 , 0 
        s = 0
        res = float('inf')
        
        for r in range(len(nums)):
            s += nums[r]
            
            while s>= target:
                res = min(res, r-l+1)
                s-=nums[l]
                l+=1
                
        return res if res!= float('inf') else 0
 
        
        