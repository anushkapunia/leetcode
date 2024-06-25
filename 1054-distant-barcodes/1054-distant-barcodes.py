class Solution(object):
    def rearrangeBarcodes(self, barcodes):

        count = Counter(barcodes)
        
        # Create a max heap of (-frequency, barcode)
        heap = [(-freq, code) for code, freq in count.items()]
        heapq.heapify(heap)
        
        result = []
        while len(heap) >= 2:
            # Pop the two most frequent barcodes
            freq1, code1 = heapq.heappop(heap)
            freq2, code2 = heapq.heappop(heap)
            
            # Add them to the result
            result.extend([code1, code2])
            
            # If there are more of these barcodes, push them back to the heap
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, code1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, code2))
        
        # If there's one barcode left, add it to the result
        if heap:
            result.append(heap[0][1])
        
        return result
        