a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
j = 0
for i in range(b):
    while j < a and arr2[i] > arr1[j]:
        j+=1
    ans.append(j)
    
print(*ans)