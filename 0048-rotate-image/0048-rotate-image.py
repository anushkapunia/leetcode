class Solution(object):
    def rotate(self, matrix):
        n = len(matrix[0])
        a = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                a[i][j] = matrix[i][j]
                
        for i in range(n):
            for j in range(n):
                matrix[i][j] = a[n-1-j][i]
                
        