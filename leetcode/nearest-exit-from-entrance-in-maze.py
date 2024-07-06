from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(i, j):
            return 0 <= i < rows and 0 <= j < cols

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            i, j, steps = queue.popleft()
            
            for x, y in directions:
                new_x, new_y = i + x, j + y
                
                if inbound(new_x, new_y) and maze[new_x][new_y] == '.':
                    if new_x in [0, rows - 1] or new_y in [0, cols - 1]:
                        return steps + 1

                    maze[new_x][new_y] = '+'
                    queue.append((new_x, new_y, steps + 1))

        return -1
