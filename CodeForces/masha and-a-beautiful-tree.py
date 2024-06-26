def merge(left, right):
    global ans
    res = []
    if left[0] <= right[0]:
        res.extend(left + right)
    else:
        res.extend(right + left)
        ans += 1
    return res
 
def merge_sort(arr, l, r):
    if l >= r:
        return [arr[l]]
    m = (l + r) // 2
    left_sorted = merge_sort(arr, l, m)
    right_sorted = merge_sort(arr, m + 1, r)
    return merge(left_sorted, right_sorted)
 
t = int(input())
 
for _ in range(t):
    ans = 0
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = merge_sort(arr1, 0, n - 1)
    if sorted(arr1) == arr2:
        print(ans)
    else:
        print(-1)