class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        peak_index = arr.index(max(arr))
        n = len(arr)
        if n < 3 or peak_index == 0 or peak_index == n-1:
            return False

        for i in range(1, peak_index):
            if arr[i] <= arr[i-1]:
                return False
        
        for i in range(peak_index+1, n):
            if arr[i] >= arr[i-1]:
                return False
        return True