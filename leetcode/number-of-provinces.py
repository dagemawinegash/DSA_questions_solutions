class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        ans = 0
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1

        return ans
