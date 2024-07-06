from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n

        queue = deque([(0, 0, 1)]) 
        visited = set([(0, 0)])
        
        while queue:
            r, c, dist = queue.popleft()
            
            if (r, c) == (n - 1, n - 1):
                return dist
            
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if inbound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, dist + 1))
        
        return -1
