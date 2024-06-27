class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def merge(arr, count, s, mid, e):
            temp = []
            i, j = s, mid + 1

            while i <= mid and j <= e:
                if arr[i][0] > arr[j][0]:
                    count[arr[i][1]] += e - j + 1
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= e:
                temp.append(arr[j])
                j += 1

            for k in range(len(temp)):
                arr[s + k] = temp[k]

        def mergeSort(arr, count, l, r):
            if l >= r:
                return
            
            mid = (l + r) // 2
            mergeSort(arr, count, l, mid)
            mergeSort(arr, count, mid + 1, r)
            merge(arr, count, l, mid, r)

        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        count = [0] * n
        mergeSort(arr, count, 0, n - 1)
        return count