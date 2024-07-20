class Solution(object):
    def minSubArrayLen(self, target, nums):
 
        left = curr_sum = 0
        min_len = float('inf')
        
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
        