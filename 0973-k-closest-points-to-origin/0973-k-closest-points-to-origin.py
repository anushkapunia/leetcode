class Solution(object):
    def kClosest(self, points, k):
   
        if not points or k <= 0:
            return []
        
        h = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(h, (dist, (x, y)))
        
        r = []
        while k > 0 and h:
            _, p = heapq.heappop(h)
            r.append(list(p))
            k -= 1
        
        return r
        