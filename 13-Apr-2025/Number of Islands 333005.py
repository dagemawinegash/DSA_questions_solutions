# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def helper(i, j):
            if not inbound(i, j) or grid[i][j] == "0":
                return False

            grid[i][j] = "0"

            for x, y in directions:
                new_x, new_y = i + x, j + y
                helper(new_x, new_y)
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    ans += 1
                    helper(i, j)
        return ans