# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            y = nums[i + 1]
            z = nums[i + 2]
            if z + y > x:
                return x + y + z
        return 0
        