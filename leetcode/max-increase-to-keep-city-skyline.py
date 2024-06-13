class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        c = r = len(grid)
        ans = 0

        rows = [max(row) for row in grid]
        cols = [max(grid[j][i] for j in range(r)) for i in range(c)]
        
        for i in range(c):
            for j in range(r):
                y = min(rows[i], cols[j])
                ans += y - grid[i][j]
        
        return ans