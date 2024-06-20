class Solution(object):
    def frequencySort(self, s):
        char_freq = Counter(s)
        
        # Create a list of buckets, where each bucket represents a frequency
        buckets = [[] for _ in range(len(s) + 1)]
        
        # Populate the buckets with characters and their frequencies
        for char, freq in char_freq.items():
            buckets[freq].append(char * freq)
        
        # Build the answer string by iterating over the buckets in reverse order
        answer = ''.join(char for bucket in reversed(buckets) for char in bucket)
        
        return answer
        