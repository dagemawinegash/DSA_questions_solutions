# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
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
        
        n = len(graph)
        color = [-1] * n

        for node in range(n):
            if color[node] == -1:
                color[node] = 1
                if not helper(node):
                    return False
        return True
