class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        right, i, ans = 0, 0, 0
        while right < n:
            if i < len(nums) and nums[i] <= right + 1:
                right += nums[i]
                i += 1
            else:
                ans += 1
                right += (right + 1)
        return ans