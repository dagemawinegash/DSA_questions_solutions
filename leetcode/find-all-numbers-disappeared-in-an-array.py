class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        def cycleSort(nums):
            n = len(nums)
            i = 0
            while i < n:
                correct_position = nums[i] - 1
                if nums[i] != nums[correct_position]:
                    nums[correct_position], nums[i] = nums[i], nums[correct_position]
                else:
                    i += 1
        
        cycleSort(nums)
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                ans.append(i + 1)
        
        return ans