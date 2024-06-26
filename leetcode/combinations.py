class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
            return
        
        backtrack(1, [])
        return ans