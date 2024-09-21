class Solution(object):
    def topKFrequent(self, words, k):
        d = Counter(words)
        l = []
        for w,f in d.items():
            heapq.heappush(l, (-f,w))
        
        a = []        
        while k > 0:
            f , w = heapq.heappop(l)
            a.append(w)
            k-=1
            
        return a
            
            
        