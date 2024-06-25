class Solution(object):
    def rearrangeBarcodes(self, barcodes):

        n = len(barcodes)
        if n < 2:
            return barcodes

        # Count the frequency of each barcode
        count = Counter(barcodes)
        
        # Find the most common element
        max_count, max_elem = max((count[x], x) for x in count)
        
        # Create the result array
        result = [0] * n
        
        # Start filling the even indices with the most common element
        idx = 0
        for _ in range(max_count):
            result[idx] = max_elem
            idx += 2
            if idx >= n:
                idx = 1  # Switch to odd indices if we reach the end
        
        # Fill the remaining positions with other elements
        for num in count:
            if num != max_elem:
                for _ in range(count[num]):
                    if idx >= n:
                        idx = 1
                    result[idx] = num
                    idx += 2
        
        return result
        