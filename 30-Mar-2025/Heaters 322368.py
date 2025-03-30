# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def checker(radius):
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if heaters[j] - radius <= houses[i] <= heaters[j] + radius:
                    i += 1
                else:
                    j += 1
            return i == len(houses)

        l = 0
        r = max(houses[-1], heaters[-1])
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans