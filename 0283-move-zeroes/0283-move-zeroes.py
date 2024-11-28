class Solution(object):
    def moveZeroes(self, nums):
        j = -1
        n = len(nums)
        for j in range(n):
            if nums[j] == 0:
                break
                
        if j ==-1:
            return
        
        for i in range(j+1,n):
            if nums[i]!=0:
                nums[i] , nums[j] = nums[j] , nums[i]
                j+=1
                
        