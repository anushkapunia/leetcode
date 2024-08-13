class Solution(object):
    def majorityElement(self, nums):
       
        counts = {}
        majority_count = len(nums) // 2
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > majority_count:
                return num
