n = int(input())
adj_matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if adj_matrix[i][j] == 1:
            ans += 1

print(ans)
