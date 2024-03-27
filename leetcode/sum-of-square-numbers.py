class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(sqrt(c))
        for a in range(sqrt_c+1):
            b = sqrt(c-a**2)
            if b == int(b):
                return True
        return False
        