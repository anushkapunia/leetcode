class Solution(object):
     def maxDistance(self, A):
        i=0
        j =  len(A) - 1
        while A[0] == A[j]: 
            j -= 1
        while A[-1] == A[i]: 
            i += 1
        return max(len(A) - 1 - i, j)