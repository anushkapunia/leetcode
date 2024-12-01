class Solution(object):
    def intersect(self, nums1, nums2):
        if nums1 > nums2 :
            nums2 , nums1 = nums1 , nums2
            
        c = {}
        
        for n in nums1:
            c[n] = c.get(n,0) +1
            
        r = []    
        for n in nums2:
            if n in c:
                r.append(n)
                c[n]-=1
                if c[n] == 0:
                    del c[n]
                    
        return r
            