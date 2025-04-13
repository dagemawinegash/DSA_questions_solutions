# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def helper(i, j):
            if not inbound(i, j) or grid2[i][j] == 0:
                return True

            grid2[i][j] = 0
            is_sub = grid1[i][j] == 1

            for x, y in directions:
                new_x, new_y = i + x, j + y
                if not helper(new_x, new_y):
                    is_sub = False
            return is_sub
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if helper(i, j):
                        ans += 1
                    
        return ans