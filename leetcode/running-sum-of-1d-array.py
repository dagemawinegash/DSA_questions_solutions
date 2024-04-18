class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_array = [sum(nums[:i]) for i in range(1,len(nums)+1)]
        return sum_array