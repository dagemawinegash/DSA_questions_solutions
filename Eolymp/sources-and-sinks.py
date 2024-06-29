n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

sources = []
sinks = []

for i in range(n):
    is_source = True
    for j in range(n):
        if graph[j][i] == 1:
            is_source = False
            break
    if is_source:
        sources.append(i + 1)  

for i in range(n):
    is_sink = True
    for j in range(n):
        if graph[i][j] == 1:
            is_sink = False
            break
    if is_sink:
        sinks.append(i + 1)  

print(len(sources), ' '.join(map(str, sources)))
print(len(sinks), ' '.join(map(str, sinks)))
