class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def subarray_gcd(start):
            res = nums[start]
            count = 0
            for end in range(start, len(nums)):
                res = gcd(res, nums[end])
                if res == k:
                    count += 1
            return count
        
        ans = 0
        for start in range(len(nums)):
            ans += subarray_gcd(start)
        
        return ans