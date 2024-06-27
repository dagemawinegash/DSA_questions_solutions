class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def cycleSort(arr):
            n = len(arr)
            i = 0
            while i < n:
                correct_position = arr[i] - 1
                if arr[i] != arr[correct_position]:
                    arr[correct_position], arr[i] = arr[i], arr[correct_position]
                else:
                    i += 1
            return arr
        
        nums = cycleSort(nums)
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]

        