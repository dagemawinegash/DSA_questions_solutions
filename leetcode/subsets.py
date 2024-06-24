class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, subset):
            ans.append(subset[:])
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        ans = []
        backtrack(0, [])
        return ans
