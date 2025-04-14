# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
    
        def helper(node):
            visited[node] = 1
            for neighbour in range(n):
                if isConnected[node][neighbour] and not visited[neighbour]:
                    helper(neighbour)

        ans = 0
        visited = [0] * (n)
        for node in range(n):
            if not visited[node]:
                ans += 1
                helper(node)
        return ans