class Solution(object):
    def findPeakElement(self, nums):
        
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
        
            if nums[mid] > nums[mid + 1]:
            # Peak is in the left half
                right = mid
            else:
            # Peak is in the right half
                left = mid + 1
    
    # At the end of the loop, left == right, which will be the peak element
        return left

        