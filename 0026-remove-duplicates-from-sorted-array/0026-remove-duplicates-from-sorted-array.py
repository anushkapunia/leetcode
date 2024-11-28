class Solution(object):
    def removeDuplicates(self, nums):
        l = []
        for n in nums:
            if n in l:
                continue
            else:
                l.append(n)
                
        for i in range(len(l)):
            nums[i] = l[i]
            
        return len(l)
            
                
        
        
        
        