class Solution:    
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(x, y):
            if y == 0:
                return 1
            half = power(x, y // 2)
            half = (half * half) % MOD
            if y % 2 != 0:
                half = (half * x) % MOD
            return half
        
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        return (power(5, even_count) * power(4, odd_count)) % MOD