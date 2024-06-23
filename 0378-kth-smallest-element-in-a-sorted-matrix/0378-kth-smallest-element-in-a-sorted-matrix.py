class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []
        
        # Add the first element of each row to the min-heap
        for r in range(min(k, n)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # Pop from the heap k times
        while k > 0:
            val, r, c = heapq.heappop(min_heap)
            
            # If there are more elements in this row, add the next one
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
            
            k -= 1
        
        return val
        