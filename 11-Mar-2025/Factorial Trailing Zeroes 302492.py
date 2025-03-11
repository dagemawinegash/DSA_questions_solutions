# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(x):
            if x > n: return 0
            return (n // x) + (helper(x * 5)) 
        return helper(5)
    