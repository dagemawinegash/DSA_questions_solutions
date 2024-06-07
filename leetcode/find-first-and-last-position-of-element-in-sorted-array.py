from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1

        if l <= r and nums[l] == target and nums[r] == target:
            return [l, r]
        return [-1, -1]