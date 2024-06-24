class Solution(object):
    def lastStoneWeight(self, stones):
    
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            if x < y:
                heapq.heappush(heap, x - y)
        
        return -heap[0] if heap else 0