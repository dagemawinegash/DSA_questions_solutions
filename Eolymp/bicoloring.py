from collections import defaultdict

def helper(n):
    e = int(input())
    graph = defaultdict(list)
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node):
        for neighbour in graph[node]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[node]
                if not dfs(neighbour):
                    return False
            elif color[neighbour] == color[node]:
                return False
        return True
    
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            if not dfs(i):
                return "NOT BICOLOURABLE."
    
    return "BICOLOURABLE."

while True:
    n = int(input())
    if n == 0:
        break
    ans = helper(n)
    print(ans)
