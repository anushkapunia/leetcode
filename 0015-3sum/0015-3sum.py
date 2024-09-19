class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        s = set()
        for i in range(len(nums)-2):
            n = nums[i]
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            
            while l<r:
                v =  nums[i] + nums[l] +nums[r]
                if v == 0:
                    s.add((nums[i]  , nums[l] , nums[r]))
                    
                    while l <r and nums[r] == nums[r-1]:
                        r-=1
                      
                    while l <r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
                elif v > 0:
                  
                    r-=1
                else:
                   
                    l+=1
        return [list(x) for x in s]
                    


        