# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = sum(candies)
        ans = 0
        def checker(curr_max):
            res = 0
            for num in candies:
                res += num // curr_max
            return res >= k
        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid 
                l = mid + 1
            else:
                r = mid - 1
        return ans