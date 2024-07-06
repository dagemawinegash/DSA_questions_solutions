from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        ans = [[float('inf')] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()

            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if inbound(new_x, new_y) and ans[new_x][new_y] == float('inf'):
                    queue.append((new_x, new_y))
                    ans[new_x][new_y] = ans[i][j] + 1
        
        return ans
