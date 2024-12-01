class Solution(object):
    def rearrangeArray(self, nums):
        p = []
        n = []
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        a = []
        i = 0
        j = 0
        while i < len(p) and j < len(n):
            a.append(p[i])
            a.append(n[j])
            i+=1
            j+=1

        return a

        
        