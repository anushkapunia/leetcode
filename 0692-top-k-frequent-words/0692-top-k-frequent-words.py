class Solution(object):
    def topKFrequent(self, words, k):
        w = Counter(words)
        
        s = sorted(w , key = lambda x : (-w[x] , x)) 
        
        return s[:k]