# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n):
            if n == 1:
                return True
            if n < 1:
                return F
            return helper(n / 4)
        return helper(n)
        