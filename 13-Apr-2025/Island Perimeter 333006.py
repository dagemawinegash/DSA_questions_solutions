# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def helper(i, j):
            nonlocal ans
            if visited[i][j]:
                return 

            visited[i][j] = True

            for x, y in directions:
                new_x, new_y = x + i, y + j
                if not inbound(new_x, new_y) or not grid[new_x][new_y]:
                    ans += 1
                elif not visited[new_x][new_y]:
                    helper(new_x, new_y)
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    helper(i, j)
                    return ans

    