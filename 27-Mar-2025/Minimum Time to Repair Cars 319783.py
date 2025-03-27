# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 0
        r = max(ranks) * cars * cars
        ans = 0
        def checker(curr_time):
            res = 0
            for num in ranks:
                res += floor(sqrt(curr_time / num))
            return res >= cars
        
        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans