class Solution(object):
    def matrixScore(self, grid):
        
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 1 - grid[r][c]

        for c in range(1, n):
            z = 0
            for r in range(m):
                if grid[r][c] == 0:
                    z += 1
            if z > m - z:
                for r in range(m):
                    grid[r][c] = 1 - grid[r][c]

        s = 0
        for c in range(n):
            o = 0
            for r in range(m):
                if grid[r][c] == 1:
                    o += 1
            s += o * 2 ** (n - c - 1)
        return s
        