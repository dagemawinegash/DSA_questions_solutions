# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # print(graph)

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()      
            if node == destination:
                return True
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        return False
        

