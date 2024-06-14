from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            hour = 0
            
            for pile in piles:
                hour += ceil(pile / mid)
            
            if hour <= h:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans