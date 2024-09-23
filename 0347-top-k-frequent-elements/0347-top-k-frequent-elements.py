class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == k:
            return list(set(nums))
        
        d = Counter(nums)
        b = [[] for _ in range(len(nums)+1)]
        
        for e , f in d.items():
            b[f].append(e)
        r = []    
        for i in range(len(b)-1 , 0 , -1):
            for n in b[i]:
                
                r.append(n)
                if len(r) == k:
                    return r

            