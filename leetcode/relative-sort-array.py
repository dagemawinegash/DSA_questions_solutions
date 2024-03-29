class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        set_arr2 = set(arr2)
        ans = []
        for num in arr2:
            count = arr1.count(num)
            for _ in range(count):
                ans.append(num)
        notin_arr2 = []
        for num in arr1:
            if num not in set_arr2:
                notin_arr2.append(num)
        notin_arr2.sort()
        ans.extend(notin_arr2)
        return ans
