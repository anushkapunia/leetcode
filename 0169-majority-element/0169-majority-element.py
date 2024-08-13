class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for n in nums:
            if n in d:
                d[n] +=1
            else:
                d[n] = 0
        h = []        
        for a , b in d.items():
            heapq.heappush(h , (-b , a))
            
        return h[0][1]
            
        