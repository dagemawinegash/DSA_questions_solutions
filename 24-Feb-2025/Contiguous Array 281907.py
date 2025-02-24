# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        ones = 0
        zeros = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0: zeros += 1
            else: ones += 1

            if zeros - ones not in d:
                d[zeros - ones] = i
            if zeros == ones:
                ans = zeros + ones
            else:
                idx = d[zeros - ones]
                ans = max(ans, i - idx)
        return ans
        