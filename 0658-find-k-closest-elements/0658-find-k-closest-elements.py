class Solution(object):
    def findClosestElements(self, arr, k, x):
       
        heap = []
        
        for num in arr:
            diff = abs(num - x)
            
            # If the heap size is less than k, add the current element
            if len(heap) < k:
                heapq.heappush(heap, (-diff, -num))
            else:
                # If the current element is closer than the farthest element in the heap
                if diff < -heap[0][0] or (diff == -heap[0][0] and num < -heap[0][1]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-diff, -num))
        
        # Extract the numbers from the heap and sort them
        result = sorted(-num for _, num in heap)
        return result
        