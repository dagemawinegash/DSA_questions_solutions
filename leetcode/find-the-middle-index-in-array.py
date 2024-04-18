class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        sum_array = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sum_array[i] = sum_array[i - 1] + nums[i - 1]

        for i in range (len(nums)):
            if sum_array[i] == sum_array[len(nums)] - sum_array[i+1]:
                return i
        return -1