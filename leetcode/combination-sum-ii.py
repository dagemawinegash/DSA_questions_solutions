class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        
        def backtrack(i, arr, num):
            if num == target:
                ans.append(arr[:])
                return 
            if i >= len(candidates) or num > target:
                return

            arr.append(candidates[i])
            backtrack(i + 1, arr, num + candidates[i])
            arr.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, arr, num)

        candidates.sort()
        backtrack(0, [], 0)
        return ans
