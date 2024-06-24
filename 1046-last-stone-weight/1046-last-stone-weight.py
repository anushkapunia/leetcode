class Solution(object):
    def lastStoneWeight(self, stones):
        s = [-a for a in stones]
        heapq.heapify(s)
        
        while len(s) > 1:
            s1 = heapq.heappop(s)
            s2 = heapq.heappop(s)
            
            if s1 == s2:
                pass
            elif -s2 < -s1 :
                heapq.heappush(s , -(-s1 - (-s2)))
                
        if len(s) == 1:
            return -s[0]
        else:
            return 0
        
            
        
        