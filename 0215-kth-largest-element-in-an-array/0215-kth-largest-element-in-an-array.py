class Solution(object):
    def findKthLargest(self, nums, k):
       
        largest = float('-inf')
        for num in nums:
            if num > largest:
                largest = num
        freq = {}
        for num in nums:
            diff = largest - num
            if diff in freq:
                freq[diff] += 1
            else:
                freq[diff] = 1
        count = 0
        diff = 0
        while count < k:
            count += freq.get(diff, 0)
            diff += 1

        return largest - diff + 1
        