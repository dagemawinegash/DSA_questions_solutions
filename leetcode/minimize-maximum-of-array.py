from math import ceil

class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        ans = nums[0]
        SUM = nums[0]
        for i in range(1, len(nums)):
            SUM += nums[i]
            val = ceil(SUM / (i + 1))
            if val > ans:
                ans = val
        return ans
        