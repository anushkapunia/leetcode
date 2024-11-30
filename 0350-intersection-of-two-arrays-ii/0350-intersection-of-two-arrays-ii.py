class Solution(object):
    def intersect(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        if (n > m):
            v = [0]*n
        else:
            v = [0]*m
        a = []    
        for i in range(n):
            for j in range(m):
                if (nums1[i] == nums2[j] and v[j] == 0):
                    a.append(nums1[i])
                    v[j] = 1
                    break
                
        return a
                    