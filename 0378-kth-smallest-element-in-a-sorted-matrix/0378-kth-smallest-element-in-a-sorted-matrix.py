class Solution(object):
    def kthSmallest(self, matrix, k):
        
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        
        def count_less_equal(target):
            count = 0
            c = n - 1  # start from the rightmost column
            for r in range(n):
                while c >= 0 and matrix[r][c] > target:
                    c -= 1
                count += c + 1
            return count
        
        while left < right:
            mid = left + (right - left) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
        

        