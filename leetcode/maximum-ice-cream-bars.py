class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        sum_costs,ans = 0,0
        costs.sort()  
        for i in range(len(costs)):
            sum_costs += costs[i]
            if sum_costs <= coins:
                ans+=1
        return ans
        