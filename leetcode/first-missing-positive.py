class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        def cycleSort(nums):
            n = len(nums)
            i = 0
            while i < n:
                correct_position = nums[i] - 1
                if 1 <= nums[i] <= n and nums[i] != nums[correct_position]:
                    nums[correct_position], nums[i] = nums[i], nums[correct_position]
                else:
                    i += 1
               
        cycleSort(nums)
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1