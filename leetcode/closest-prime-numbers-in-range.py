from math import sqrt

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(sqrt(right)) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        ans = [-1, -1]
        min_gap = float('inf')
        
        for i in range(len(primes) - 1):
            num1 = primes[i]
            num2 = primes[i + 1]
            gap = num2 - num1
            if gap < min_gap:
                min_gap = gap
                ans = [num1, num2]
        
        return ans
        