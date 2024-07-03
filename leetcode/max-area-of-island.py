class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(x, y):
            nonlocal area
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return
            area += 1
            grid[x][y] = 0  
            for dr, dc in directions:
                new_x = x + dr
                new_y = y + dc
                dfs(new_x, new_y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(area, max_area)

        return max_area
