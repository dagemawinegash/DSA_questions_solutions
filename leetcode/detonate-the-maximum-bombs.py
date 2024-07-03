from math import sqrt
from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)

        def dfs(bomb, visited):
            nonlocal count
            visited.add(bomb)
            count += 1
            for neighbor in graph[bomb]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        ans = 0
        for i in range(n):
            count = 0
            dfs(i, set())
            ans = max(ans, count)
        
        return ans
