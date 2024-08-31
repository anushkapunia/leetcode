class Solution(object):
    def searchMatrix(self, matrix, t):
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        h = (m*n)-1
        while l <= h:
            mi = (l+h)//2
            
            if t == matrix[ mi//n][ mi % n ]:
                return True
            elif t < matrix[ mi//n ][ mi % n ]:
                h = mi-1
            else:
                l = mi+1
                
        return False
        