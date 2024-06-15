class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return '0'
            length = (2 ** n) - 1
            mid = length // 2 + 1
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                k = length - k + 1
                return '1' if helper(n - 1, k) == '0' else '0'
        
        return helper(n, k)



        