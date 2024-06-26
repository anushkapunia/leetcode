class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        return list(set(num for num in nums2 if num in set1))
        