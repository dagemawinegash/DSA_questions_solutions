# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 0
        r = 2 * max(bloomDay)

        def checker(days):
            count = 0
            res = 0
            for num in bloomDay:
                if num <= days:
                    count += 1
                else:
                    res += count // k
                    count = 0
            res += count // k
            return res >= m
        
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2

            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans