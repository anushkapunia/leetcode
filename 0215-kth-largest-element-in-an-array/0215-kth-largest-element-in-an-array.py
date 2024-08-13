class Solution(object):
    def findKthLargest(self, nums, k):
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h , n)
            elif h[0] < n:
                heapq.heappop(h)
                heapq.heappush(h , n)
                
                
        return h[0]