class Solution(object):
    def merge(self, nums1, m, nums2, n):
         p1, p2, p = m - 1, n - 1, m + n - 1
    
    # While there are elements to compare in both arrays
         while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
    
    # If there are any remaining elements in nums2, place them in nums1
         while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
       