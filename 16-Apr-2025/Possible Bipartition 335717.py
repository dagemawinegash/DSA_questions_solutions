# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def helper(node):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    if not helper(neighbour):
                        return False
                else:
                    if color[neighbour] == color[node]:
                        return False
            return True
        
        color = [-1] * (n + 1)
        
        for node in range(1, n + 1):
            if color[node] == -1:
                color[node] = 1
                if not helper(node):
                    return False
        # print(color)
        return True
