class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        ans = []
        n = len(arr)
        for i in range(len(arr)):
            max_element = max(arr[:n-i])
            max_index = arr.index(max_element)+1 
            ans.append(max_index)
            arr[:max_index] = arr[:max_index][::-1]
            arr[:n-i] = arr[:n-i][::-1]
            ans.append(n-i)
        return ans