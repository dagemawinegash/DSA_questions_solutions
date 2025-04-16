# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [[] for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        def helper(ancestor, node, visited):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    ans[neighbour].append(ancestor)
                    helper(ancestor, neighbour, visited)
  
        for node in range(n):
            helper(node, node, set())
        return ans
        