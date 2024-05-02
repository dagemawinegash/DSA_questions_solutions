class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = 0
        ans = []

        for i, num in enumerate(nums):
            right_sum = total - num - left_sum
            value = num * i - left_sum + right_sum - num * (len(nums) - i - 1)
            ans.append(value)
            left_sum += num
        
        return ans