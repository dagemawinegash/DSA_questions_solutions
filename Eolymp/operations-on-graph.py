from collections import defaultdict

n = int(input())
k = int(input())

graph = defaultdict(list)

for _ in range(k):
    row = list(map(int, input().split()))
    if row[0] == 1:
        u = row[1]
        v = row[2]
        graph[u].append(v)
        graph[v].append(u)
    else:
        arr = graph[row[1]]
        print(*arr)

    


    


