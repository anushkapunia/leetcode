class Solution(object):
    def removeDuplicates(self, nums):
        l = list(set(nums))
        s = sorted(l)
        
        for i in range(len(s)):
            nums[i] = s[i]
            
        
        return len(s)
            
                
        
        
        
        