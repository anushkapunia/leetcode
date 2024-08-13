class Solution(object):
    def majorityElement(self, nums):
        c = Counter(nums)
        
        return max(c.keys() , key = c.get)
       
        
