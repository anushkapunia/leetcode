class Solution(object):
    def topKFrequent(self, nums, k):
        # Count the frequency of each number
        count = Counter(nums)
        
        # Sort the items by frequency in descending order and return the k most common
        return [item[0] for item in count.most_common(k)]
        