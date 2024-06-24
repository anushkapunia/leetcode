class Solution(object):
    def topKFrequent(self, words, k):
        word_counts = Counter(words)
    
    # Sort the words based on frequency (descending) and lexicographical order
        sorted_words = sorted(word_counts, key=lambda x: (-word_counts[x], x))
    
    # Return the top k words
        return sorted_words[:k]
        
        