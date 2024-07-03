class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        
        color = [-1] * (n + 1)  

        def dfs(node):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    if not dfs(neighbour):
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True

        for i in range(1, n + 1): 
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
