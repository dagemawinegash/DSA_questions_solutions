# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n, x):
            if n == 0:
                return 1
            
            num = helper(n // 2, x)
            ans = num * num
            if n % 2:
                ans = ans * x
            return ans
        ans = helper(abs(n), x)
        return ans if n >= 0 else 1 / ans

        