# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        l = 0
        r = max(position)
        position.sort()
        
        def checker(poss_ans):
            res = 1
            curr_force = position[0]
            for num in position[1:]:
                if num - curr_force >= poss_ans:
                    res += 1
                    curr_force = num
            return res >= m

        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if checker(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans