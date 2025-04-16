# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def helper(i, j):
            if not inbound(i, j) or not grid[i][j]:
                return 0

            grid[i][j] = 0
            count = 1
            for x, y in directions:
                new_x, new_y = i + x, j + y
                count += helper(new_x, new_y)
            return count
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ans = max(ans, helper(i, j))
                    
        return ans