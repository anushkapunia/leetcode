class Solution(object):
    def intersection(self, nums1, nums2):
        s = set()
        for n in nums1:
            for m in nums2:
                if n == m:
                    s.add(n)
                
        return s
            
        