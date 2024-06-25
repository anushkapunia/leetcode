class Solution(object):
    def minSetSize(self, arr):
   
        n = len(arr)
        counts = sorted(Counter(arr).values(), reverse=True)
        
        removed = 0
        for i, count in enumerate(counts, 1):
            removed += count
            if removed >= n // 2:
                return i