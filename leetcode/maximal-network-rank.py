class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                curr = len(graph[i]) + len(graph[j])
                if i in graph[j] or j in graph[i]:
                    curr -= 1
                ans = max(ans, curr)
        return ans


