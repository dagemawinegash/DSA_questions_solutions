class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        ans = 0
        for i in range (len(piles)//3, len(piles)-1,2):
            ans+=piles[i]
        return ans