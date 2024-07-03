class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid1)
        cols = len(grid1[0])
        ans = 0
        
        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        def dfs(x, y):
            if not inbound(x, y) or grid2[x][y] == 0:
                return True
            
            grid2[x][y] = 0
            is_sub = grid1[x][y] == 1
            
            for dr, dc in directions:
                new_x = x + dr
                new_y = y + dc
                if not dfs(new_x, new_y):
                    is_sub = False
            
            return is_sub

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        ans += 1
        
        return ans
