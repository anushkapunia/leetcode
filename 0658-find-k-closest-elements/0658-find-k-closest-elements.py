class Solution(object):
    def findClosestElements(self, arr, k, x):
        
        return sorted(heapq.nsmallest(k, arr, key=lambda i: abs(i-x+.1)))
        