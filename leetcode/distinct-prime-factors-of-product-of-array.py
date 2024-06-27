class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        distinct = set()
        for n in nums:
            divisor = 2
            while n >= 2:
                if n % divisor == 0:
                    distinct.add(divisor)
                    n //= divisor
                else:
                    divisor += 1
        return len(distinct)