# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda item:item[0] - item[1])
        ans = 0
        n = len(costs)

        for i in range(n):
            if i < n // 2: ans += costs[i][0]
            else: ans += costs[i][1]
        return ans
            
       