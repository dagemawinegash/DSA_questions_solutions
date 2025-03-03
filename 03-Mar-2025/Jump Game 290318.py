# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= curr:
                curr = i
        if curr == 0:
            return True      
        return False
        