class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        
        def backtrack(i, arr, num):
            if num == target:
                ans.append(arr[:])
                return 
            if i >= len(candidates) or num > target:
                return
            arr.append(candidates[i])
            backtrack(i, arr, num + candidates[i])
            arr.pop()
            backtrack(i + 1, arr, num)

        backtrack(0, [], 0)
        return ans