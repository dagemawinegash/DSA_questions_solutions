class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def helper(capacity):
            total = 0
            d = 1
            for w in weights:
                if total + w > capacity:
                    d += 1
                    total = w
                    if d > days:
                        return False
                else:
                    total += w
            return True
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
