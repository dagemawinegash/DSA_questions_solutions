# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = sum(weights) + 2

        def checker(curr_cap):
            curr_sum = 0
            res = 0
            for weight in weights:
                if weight > curr_cap:
                    return False
                curr_sum += weight
                if curr_sum > curr_cap:
                    curr_sum = weight
                    res += 1

            return res + 1 <= days
            
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            print(mid)

            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        