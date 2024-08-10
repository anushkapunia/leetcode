class Solution(object):
    def topKFrequent(self, words, k):
        d = Counter(words)
        h = []
        for a , b in d.items():
            heapq.heappush(h , (-b,a))
            
    
        
        r = []
        while k>0:
            a, b = heapq.heappop(h)
            r.append(b)
            k = k-1
            
        return r
                
            
            
        
            

        