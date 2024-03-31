class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        operations = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                operations += i+1
        return operations