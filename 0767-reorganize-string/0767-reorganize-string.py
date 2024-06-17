from collections import Counter
import heapq

class Solution(object):
    def reorganizeString(self, s):
        # Count the frequency of each character
        char_counts = Counter(s)
        
        # Create a max heap (using negated counts for max heap behavior)
        heap = [(-count, char) for char, count in char_counts.items()]
        heapq.heapify(heap)
        
        # If the most frequent character appears more than (n+1)/2 times,
        # it's impossible to reorganize
        if -heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        result = []
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            
            result.extend([char1, char2])
            
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))
        
        if heap:
            result.append(heap[0][1])
        
        return ''.join(result)
    