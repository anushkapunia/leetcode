class Solution(object):
    def moveZeroes(self, nums):
        non = 0
        
        if nums == [0]:
            return nums
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i] , nums[non] = nums[non] , nums[i]
                non+=1
                
        
                
        