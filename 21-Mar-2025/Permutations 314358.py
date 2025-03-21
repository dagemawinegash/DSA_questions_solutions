# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        checked = [False] * n
        def helper(perms):
            if len(perms) == n:
                ans.append(perms[:])
            
            for i in range(n):
                if checked[i]:
                    continue
                checked[i] = True
                # choosing the current element
                perms.append(nums[i])
                helper(perms)
                # backtracking to the previous decision point
                checked[i] = False
                perms.pop()
        ans = []
        helper([])
        return ans
