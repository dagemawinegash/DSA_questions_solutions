from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n
        
        def dfs(i, j):
            if not inbound(i, j) or (i, j) in visited or grid[i][j] == 0:
                return
            
            visited.add((i, j))
            for dx, dy in directions:
                new_x = i + dx
                new_y = j + dy
                dfs(new_x, new_y)
        
        def bfs():
            queue = deque(visited)
            steps = 0 
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for dx, dy in directions:
                        new_x = i + dx
                        new_y = j + dy
                        if not inbound(new_x, new_y) or (new_x, new_y) in visited:
                            continue
                        if grid[new_x][new_y] == 1:
                            return steps
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
                steps += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs()
