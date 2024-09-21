class Solution(object):
    def topKFrequent(self, nums, k):
        d = Counter(nums)
        l = []
        for w , f in d.items():
            heapq.heappush(l , (f , w))
            if len(l) >k :
                heapq.heappop(l)
                
        a = []
        while k > 0:
            f,w = heapq.heappop(l)
            a.append(w)
            k-=1
    
        return a
                
            
        