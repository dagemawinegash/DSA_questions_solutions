class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        def merge(items, s, m, e, lesser, greater):
            low = s
            high = s
            for i in range(m + 1, e + 1):
                while low <= m and items[low][0] < items[i][0]:
                    low += 1
                while high <= m and items[high][0] <= items[i][0]:
                    high += 1
                lesser[items[i][1]] += low - s
                greater[items[i][1]] += m - high + 1

            temp = []
            i = s
            j = m + 1

            while i <= m and j <= e:
                if items[i][0] < items[j][0]:
                    temp.append(items[i])
                    i += 1
                else:
                    temp.append(items[j])
                    j += 1

            while i <= m:
                temp.append(items[i])
                i += 1

            while j <= e:
                temp.append(items[j])
                j += 1

            for k in range(len(temp)):
                items[s + k] = temp[k]

        def mergeSort(items, l, r, lesser, greater):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(items, l, m, lesser, greater)
            mergeSort(items, m + 1, r, lesser, greater)
            merge(items, l, m, r, lesser, greater)

        MOD = 10**9 + 7
        n = len(instructions)
        ans = 0
        items = []
        lesser = [0] * n
        greater = [0] * n

        for i in range(n):
            items.append((instructions[i], i))

        mergeSort(items, 0, n - 1, lesser, greater)

        for i in range(n):
            ans += min(lesser[i], greater[i])
            ans %= MOD

        return ans
