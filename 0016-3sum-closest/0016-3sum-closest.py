class Solution(object):
    def threeSumClosest(self, nums, target):
        fs = float('inf')
        n = len(nums)
        nums.sort()
        
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            l = i+1
            r = n-1
            
            while l<r:
                cs = nums[i] +nums[l] +nums[r] 
                if cs == target :
                    return cs
                
                if abs(cs- target) < abs(fs-target):
                    fs = cs
                elif cs > target:
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    r-=1
                else:
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    
        return fs
        
        
        
        