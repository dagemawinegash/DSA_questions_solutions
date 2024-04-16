class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float('inf')
        start, SUM = 0, 0
        for end in range(len(nums)):
            SUM += nums[end]
            while SUM >= target:
                ans = min(ans, end - start + 1)
                SUM -= nums[start]
                start += 1
        return 0 if ans == float('inf') else ans