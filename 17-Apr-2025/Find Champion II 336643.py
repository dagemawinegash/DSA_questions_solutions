# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        if n - len(graph) != 1:
            return -1
        for node in range(n):
            if node not in graph:
                return node
