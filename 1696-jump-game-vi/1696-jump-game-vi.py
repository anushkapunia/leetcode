class Solution(object):
    def maxResult(self, nums, k):
     
				n = len(nums)
				D = [-float('inf')] * (n)
				heap = [(-nums[0], 0)]
				D[0] = nums[0]   
				for i in range(1,n):
					(maxValue, index) = heap[0]            
					while index < i - k:
						heapq.heappop(heap)
						(maxValue, index) = heap[0]

					D[i] = -maxValue + nums[i]
					heapq.heappush(heap, (-D[i], i))

				return D[n-1]
        