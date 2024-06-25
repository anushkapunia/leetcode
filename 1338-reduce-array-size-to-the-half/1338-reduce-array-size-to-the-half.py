class Solution(object):
    def minSetSize(self, arr):

        c = Counter(arr)
        h = [(-n, num) for num, n in c.items()]
        heapq.heapify(h)
        
        total = 0
        removed = 0
        n = len(arr)
        
        while removed < n // 2:
            count, _ = heapq.heappop(h)
            removed += -count
            total += 1
        
        return total
        
        