# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checker(curr_k):
            res = 0
            for pile in piles:
                res += ceil(pile / curr_k)
            return res <= h
        
        l = 1
        r = 2 * 1000_000_000
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2

            if checker(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
        
            
