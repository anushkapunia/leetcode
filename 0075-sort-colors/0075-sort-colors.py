class Solution(object):
    def sortColors(self, nums):

        heapq.heapify(nums)  # Convert the list to a heap in-place
        sorted_list = []
        while nums:
            sorted_list.append(heapq.heappop(nums))
        
        # Copy sorted elements back to the original list
        for i in range(len(sorted_list)):
            nums.append(sorted_list[i])
