class Solution(object):
    def hIndex(self, citations):
        
        citations.sort(reverse=True)  # Sort in descending order
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break
        return h
        