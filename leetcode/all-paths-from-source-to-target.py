from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        Graph = defaultdict(list)
        for i, edges in enumerate(graph):
            Graph[i] = edges

        n = len(Graph)
        target = n - 1
        ans = []

        def dfs(curr_path, node):
            curr_path.append(node)
            if node == target:
                ans.append(curr_path[:])
            
            for neighbour in graph[node]:
                dfs(curr_path, neighbour)
            curr_path.pop()
        
        dfs([], 0)
        return ans
