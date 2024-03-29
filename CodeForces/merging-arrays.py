line = input()
values = line.split()
x = int(values[0])
y = int(values[1])
 
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
k, p1, p2 = 0, 0, 0
c = []
while p1 < x or p2 < y:
    if p2 == y or (p1 < x and arr1[p1] < arr2[p2]):
        c.append(arr1[p1])
        k += 1
        p1 += 1
    else:
        c.append(arr2[p2])
        k += 1
        p2 += 1
print(*c)