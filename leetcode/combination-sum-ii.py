class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()
        
        def backtrack(start, path, num):
            if num == target:
                ans.append(path[:])
                return
            
            if num > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, num + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return ans
