n = int(input())
cnt = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            cnt += 1

print(cnt // 2)



