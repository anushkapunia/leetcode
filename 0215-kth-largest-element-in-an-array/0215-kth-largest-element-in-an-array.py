class Solution(object):
    def findKthLargest(self, nums, k):
  
         heap = []
    
         for num in nums:
            
        # If the heap size is less than k, just add the element
            if len(heap) < k:
                
                heapq.heappush(heap, num)
        # If the current number is greater than the smallest in the heap,
        # remove the smallest and add the current number
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    
    # The root of the heap will be the kth largest element
         return heap[0]
        