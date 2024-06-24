class Solution(object):
    def reorganizeString(self, s):
        char_counts = Counter(s)
        
        # Create a max heap (using negative counts for max heap behavior)
        heap = [(-count, char) for char, count in char_counts.items()]
        heapq.heapify(heap)
        
        # If the most frequent character appears more than (n+1)/2 times, it's impossible to reorganize
        if -heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        result = []
        prev_count, prev_char = 0, ''
        
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            count += 1
            prev_count, prev_char = count, char
        
        return ''.join(result)
        