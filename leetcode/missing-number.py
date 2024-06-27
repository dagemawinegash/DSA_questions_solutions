class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        def cycleSort(nums):
            n = len(nums)
            i = 0
            while i < n:
                correct_position = nums[i]
                if correct_position < n and correct_position != i:
                    nums[correct_position], nums[i] = nums[i], nums[correct_position]
                else:
                    i += 1
            
        cycleSort(nums)

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)
